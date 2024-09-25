from django.forms import ModelForm
from .models import Cita


class CitaForm(ModelForm):
    class Meta:
        model = Cita
        fields = "__all__"
