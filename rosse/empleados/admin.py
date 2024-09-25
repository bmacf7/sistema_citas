from django.contrib import admin
from .models import Empleado


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "telefono")
    search_fields = ("nombre", "apellido", "correo", "telefono")
    list_filter = ("nombre", "apellido", "correo", "telefono")
    list_per_page = 10


admin.site.register(Empleado, EmpleadoAdmin)
