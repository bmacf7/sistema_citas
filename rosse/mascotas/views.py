from django.shortcuts import render
from django.views.generic import ListView, FormView, DetailView
from django.urls import reverse_lazy
from .models import Mascota
from .forms import MascotaForm


class MascotaView(ListView):
    model = Mascota
    template_name = "mascotas/listado_mascotas.html"
    context_object_name = "mascotas"


class AgregarMascotaView(FormView):
    model = Mascota
    form_class = MascotaForm
    template_name = "mascotas/agregar_mascota.html"
    success_url = reverse_lazy("listado_mascotas")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DetalleMascotaView(DetailView):
    model = Mascota
    template_name = "mascotas/detalle_mascota.html"
    context_object_name = "mascota"
