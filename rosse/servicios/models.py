from django.db import models
from empleados.models import Empleado


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    realizado_por = models.ForeignKey(
        Empleado, on_delete=models.CASCADE, related_name="servicios"
    )
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    duracion = models.IntegerField()

    def __str__(self):
        return self.nombre
