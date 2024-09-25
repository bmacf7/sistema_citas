from django.db import models
from clientes.models import Cliente


class Mascota(models.Model):
    ESPECIE_CHOICES = [
        ("PERRO", "Perro"),
        ("GATO", "Gato"),
    ]

    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name="mascotas"
    )
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    especie = models.CharField(max_length=15, choices=ESPECIE_CHOICES)
    raza = models.CharField(max_length=50)
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.especie} - {self.raza}"

    class Meta:
        db_table = "mascotas"
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"
