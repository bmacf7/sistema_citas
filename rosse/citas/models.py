from django.db import models
from mascotas.models import Mascota
from empleados.models import Empleado
from servicios.models import Servicio


class Cita(models.Model):
    ESTADO_CHOICES = [
        ("AGENDADA", "Agendada"),
        ("CANCELADA", "Cancelada"),
        ("COMPLETADA", "Completada"),
    ]
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    hora = models.TimeField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)

    def __str__(self):
        return f"{self.cliente} - {self.empleado} - {self.servicio} - {self.fecha} - {self.estado}"

    class Meta:
        db_table = "citas"
        verbose_name = "Cita"
        verbose_name_plural = "Citas"
