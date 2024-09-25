from django.contrib import admin
from .models import Servicio


class ServicioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "precio", "duracion")
    search_fields = ("nombre", "descripcion", "precio", "duracion")
    list_filter = ("nombre", "descripcion", "precio", "duracion")
    list_per_page = 10
    list_editable = ("descripcion", "precio", "duracion")


admin.site.register(Servicio, ServicioAdmin)
