import datetime
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework import viewsets

from colaboradores.models import Empleado, Marcacion
from .models import FacturaNomina
from .serializers import EmpleadoSerializer, FacturaNominaSerializer


# API REST ViewSets
class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer


class FacturaNominaViewSet(viewsets.ModelViewSet):
    queryset = FacturaNomina.objects.all()
    serializer_class = FacturaNominaSerializer


# Vista principal (Panel Dashboard)
def ver_factura(request):
    return render(request, 'nomina/factura.html')


# Vista dedicada al módulo de Nóminas
def modulo_nomina(request):
    todos_empleados = Empleado.objects.all()
    
    # Por defecto en GET (al cargar la página normalmente), la lista calculada está VACÍA
    return render(request, 'nomina/modulo_nomina.html', {
        'empleados_tabla': [],
        'empleados_select': todos_empleados,
        'excel_cargado': False,
    })


# Vista para procesar el archivo Excel y generar la tabla
def cargar_excel_marcaciones(request):
    todos_empleados = Empleado.objects.all()
    
    if request.method == "POST" and request.FILES.get("archivo_excel"):
        archivo = request.FILES["archivo_excel"]
        
        try:
            # Limpiamos marcaciones previas en la base de datos
            Marcacion.objects.all().delete()
            
            df = pd.read_excel(archivo)
            
            for _, row in df.iterrows():
                emp_id = row.get("Employee ID")
                if pd.isna(emp_id):
                    continue
                
                try:
                    empleado = Empleado.objects.get(employee_id=int(emp_id))
                    dia_nombre = str(row.get("Día", "")).strip()
                    novedad = str(row.get("Novedad / Estado", "Normal")).strip()
                    
                    # Salida teórica: Domingos 08:00 AM, entre semana 11:00 AM
                    salida_teorica_def = "08:00:00" if dia_nombre.lower() == "domingo" else "11:00:00"

                    salida_real = row.get("Salida Teórica") # Marca real
                    salida_real_str = salida_teorica_def if pd.isna(salida_real) else str(salida_real)

                    Marcacion.objects.create(
                        empleado=empleado,
                        fecha=row["Fecha"],
                        dia=dia_nombre,
                        entrada_teorica="02:00:00",
                        salida_teorica=salida_teorica_def,
                        entrada_real="02:00:00",
                        salida_real=salida_real_str,
                        novedad=novedad
                    )
                except Empleado.DoesNotExist:
                    continue

            # Obtener los empleados que tienen marcaciones en este Excel procesado
            empleados_tabla = Empleado.objects.filter(marcaciones__isnull=False).distinct()
            
            messages.success(request, "¡Nómina procesada exitosamente a partir del archivo Excel cargado!")
            
            # Retornamos la misma vista renderizando la tabla con los resultados calculados
            return render(request, 'nomina/modulo_nomina.html', {
                'empleados_tabla': empleados_tabla,
                'empleados_select': todos_empleados,
                'excel_cargado': True,
            })

        except Exception as e:
            messages.error(request, f"Error al procesar el archivo Excel: {str(e)}")

    return redirect('modulo_nomina')