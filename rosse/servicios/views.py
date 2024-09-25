from django.shortcuts import render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import CrearServicioForm, EditarServicioForm
from .models import Servicio
from django.views.generic import ListView


class ListadoServicios(ListView):
    model = Servicio
    template_name = "servicios/listado_servicios.html"
    context_object_name = "servicios"


class CrearServicio(FormView):
    template_name = "servicios/crear_servicio.html"
    form_class = CrearServicioForm
    success_url = reverse_lazy("listado_servicios")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class EditarServicio(FormView):
    template_name = "servicios/editar_servicio.html"
    form_class = EditarServicioForm
    success_url = reverse_lazy("listado_servicios")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["servicio"] = Servicio.objects.get(pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        servicio = Servicio.objects.get(pk=self.kwargs["pk"])
        form.instance.id = servicio.id
        form.save()
        return super().form_valid(form)
