from django.shortcuts import render
from django.views.generic import ListView, FormView, UpdateView
from .models import Cita
from .forms import CitaForm
from django.urls import reverse_lazy


class ListadoCitasView(ListView):
    model = Cita
    template_name = "citas/listado_citas.html"
    context_object_name = "citas"


class AgendarCitaView(FormView):
    model = Cita
    template_name = "citas/agendar_cita.html"
    context_object_name = "cita"
    form_class = CitaForm
    success_url = reverse_lazy("listado_citas")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class EditarCitaView(UpdateView):
    model = Cita
    template_name = "citas/editar_cita.html"
    context_object_name = "cita"
    form_class = CitaForm
    success_url = reverse_lazy("listado_citas")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
