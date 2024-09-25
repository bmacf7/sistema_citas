from django.contrib import admin
from .models import Mascota


class MascotaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "cliente", "especie", "raza")
    search_fields = ("nombre", "especie", "raza", "cliente__nombre")
    list_filter = ("especie", "raza")


admin.site.register(Mascota, MascotaAdmin)
