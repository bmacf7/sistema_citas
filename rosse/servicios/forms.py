from django.forms import ModelForm
from .models import Servicio


class CrearServicioForm(ModelForm):
    class Meta:
        model = Servicio
        fields = "__all__"


class EditarServicioForm(ModelForm):
    class Meta:
        model = Servicio
        fields = ["precio", "duracion"]
