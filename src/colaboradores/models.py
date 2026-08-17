from django.db import models

class Empleado(models.Model):
    employee_id = models.IntegerField(unique=True, verbose_name="ID Empleado")
    cedula = models.CharField(max_length=20, unique=True, verbose_name="C.C.")
    nombre = models.CharField(max_length=150, verbose_name="Nombre Completo")
    tipo_rol = models.CharField(max_length=50, verbose_name="Tipo de Rol")  # Operativo, MYC, etc.
    cargo = models.CharField(max_length=100, verbose_name="Cargo")
    salario_basico = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Sueldo Básico")
    grupo_descanso = models.CharField(max_length=50, blank=True, null=True, verbose_name="Grupo de Descanso")

    def __str__(self):
        return f"{self.nombre} - {self.cargo}"

class HorarioSemanal(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="horarios")
    semana = models.CharField(max_length=20, choices=[('Semana 1', 'Semana 1'), ('Semana 2', 'Semana 2')])
    dia_semana = models.CharField(max_length=15)  # Lunes, Martes, etc.
    hora_entrada = models.TimeField(null=True, blank=True)
    hora_salida = models.TimeField(null=True, blank=True)
    es_descanso = models.BooleanField(default=False)