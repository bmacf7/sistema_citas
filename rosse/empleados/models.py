from django.db import models


class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=8, unique=True)
    telefono = models.CharField(max_length=10)
    correo = models.EmailField(max_length=50)
    fecha_ingreso = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
