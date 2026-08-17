from rest_framework import serializers
from colaboradores.models import Empleado
from .models import FacturaNomina

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class FacturaNominaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacturaNomina
        fields = '__all__'