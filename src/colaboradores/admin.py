from django.contrib import admin
from .models import Empleado

# Registra el modelo Empleado
admin.site.register(Empleado)

# Configuración de cabecera
admin.site.site_header = "Sistema de Nómina Pyme"

