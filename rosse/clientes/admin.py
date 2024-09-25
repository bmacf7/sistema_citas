from django.contrib import admin
from .models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "dni", "telefono", "email", "fecha_registro")
    search_fields = ("nombre", "apellido", "dni", "telefono", "email")
    list_filter = ("fecha_registro",)
    list_per_page = 10
    ordering = ("nombre", "apellido")
    list_editable = ("telefono", "email")


admin.site.register(Cliente, ClienteAdmin)
