from django.db import models


class Empleado(models.Model):
    employee_id = models.IntegerField(unique=True, verbose_name="ID Empleado")
    cedula = models.CharField(max_length=20, unique=True, verbose_name="C.C.")
    nombre = models.CharField(max_length=150, verbose_name="Nombre Completo")
    tipo_rol = models.CharField(max_length=50, verbose_name="Tipo de Rol")
    cargo = models.CharField(max_length=100, verbose_name="Cargo")
    salario_basico = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Sueldo Básico")
    hora_entrada_teorica = models.TimeField(default="02:00:00", verbose_name="Entrada Teórica")
    hora_salida_teorica = models.TimeField(default="11:00:00", verbose_name="Salida Teórica")

    def __str__(self):
        return f"{self.nombre} - {self.cargo}"

    def total_horas_extras_quincena(self):
        """Calcula el total de horas extras acumuladas en todas las marcaciones del colaborador"""
        total_extras = 0
        for marcacion in self.marcaciones.filter(novedad="Normal"):
            total_extras += marcacion.horas_extras()
        return total_extras

    # Propiedades para sincronizar los datos de la Tabla con la Factura (13 días)
    @property
    def salario_13_dias(self):
        return round((float(self.salario_basico) / 30) * 13)

    @property
    def salario_13_dias_formatted(self):
        return f"{self.salario_13_dias:,.0f}"

    @property
    def valor_extras(self):
        return round((float(self.salario_basico) / 240) * 1.25 * self.total_horas_extras_quincena())

    @property
    def total_devengado(self):
        return self.salario_13_dias + 81000 + self.valor_extras

    @property
    def total_devengado_formatted(self):
        return f"{self.total_devengado:,.0f}"

    @property
    def salud(self):
        return round(self.salario_13_dias * 0.04)

    @property
    def salud_formatted(self):
        return f"{self.salud:,.0f}"

    @property
    def pension(self):
        return round(self.salario_13_dias * 0.04)

    @property
    def pension_formatted(self):
        return f"{self.pension:,.0f}"

    @property
    def total_deducido(self):
        return self.salud + self.pension

    @property
    def total_deducido_formatted(self):
        return f"{self.total_deducido:,.0f}"

    @property
    def total_neto(self):
        return self.total_devengado - self.total_deducido

    @property
    def total_neto_formatted(self):
        return f"{self.total_neto:,.0f}"
    
    @property
    def salario_basico_formatted(self):
        return f"{float(self.salario_basico):,.0f}"


class HorarioSemanal(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="horarios")
    semana = models.CharField(max_length=20, choices=[('Semana 1', 'Semana 1'), ('Semana 2', 'Semana 2')])
    dia_semana = models.CharField(max_length=15)
    hora_entrada = models.TimeField(null=True, blank=True)
    hora_salida = models.TimeField(null=True, blank=True)
    es_descanso = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.empleado.nombre} - {self.semana} ({self.dia_semana})"


class Marcacion(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="marcaciones")
    fecha = models.DateField(verbose_name="Fecha")
    dia = models.CharField(max_length=20, verbose_name="Día")
    entrada_teorica = models.TimeField(verbose_name="Entrada Teórica")
    salida_teorica = models.TimeField(verbose_name="Salida Teórica")
    entrada_real = models.TimeField(null=True, blank=True, verbose_name="Entrada Real")
    salida_real = models.TimeField(null=True, blank=True, verbose_name="Salida Real")
    novedad = models.CharField(max_length=50, default="Normal", verbose_name="Novedad / Estado")

    def __str__(self):
        return f"{self.empleado.nombre} - {self.fecha} ({self.novedad})"

    def horas_extras(self):
        if self.salida_real and self.salida_teorica and self.novedad == "Normal":
            t_salida = self.salida_teorica.hour * 60 + self.salida_teorica.minute
            r_salida = self.salida_real.hour * 60 + self.salida_real.minute
            
            if r_salida < 300 and r_salida > 0:
                r_salida += 720
                
            diferencia = r_salida - t_salida
            return max(0, diferencia // 60)
        return 0