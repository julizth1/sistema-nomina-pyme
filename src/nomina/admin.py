from django.contrib import admin
from .models import Marcacion, FacturaNomina

@admin.register(Marcacion)
class MarcacionAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'fecha', 'hora_entrada_real', 'hora_salida_real')

@admin.register(FacturaNomina)
class FacturaNominaAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'periodo_inicio', 'periodo_fin', 'neto_recibir')