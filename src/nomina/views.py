from django.shortcuts import render

from rest_framework import viewsets
from colaboradores.models import Empleado
from .models import FacturaNomina
from .serializers import EmpleadoSerializer, FacturaNominaSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class FacturaNominaViewSet(viewsets.ModelViewSet):
    queryset = FacturaNomina.objects.all()
    serializer_class = FacturaNominaSerializer
    
def ver_factura(request):
    return render(request, 'nomina/factura.html')