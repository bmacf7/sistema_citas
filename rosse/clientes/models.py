from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=8, unique=True)
    telefono = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        db_table = "clientes"
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["nombre", "apellido"]
