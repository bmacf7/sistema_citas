from django.forms import ModelForm
from .models import Empleado


class CrearEmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = "__all__"


class EditarEmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = ["telefono", "correo"]


class EliminarEmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = "__all__"
