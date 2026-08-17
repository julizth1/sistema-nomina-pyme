from django.db import models
from colaboradores.models import Empleado

class Marcacion(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora_entrada_real = models.TimeField()
    hora_salida_real = models.TimeField()

class FacturaNomina(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    periodo_inicio = models.DateField()
    periodo_fin = models.DateField()
    dias_laborados = models.IntegerField(default=15)
    sueldo_devengado = models.DecimalField(max_digits=12, decimal_places=2)
    auxilio_transporte = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    recargo_nocturno = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    neto_recibir = models.DecimalField(max_digits=12, decimal_places=2)