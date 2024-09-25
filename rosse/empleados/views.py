from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Empleado
from .forms import CrearEmpleadoForm, EditarEmpleadoForm, EliminarEmpleadoForm


class ListaEmpleados(ListView):
    model = Empleado
    template_name = "empleados/lista_empleados.html"
    context_object_name = "empleados"


class CrearEmpleado(FormView):
    template_name = "empleados/crear_empleado.html"
    form_class = CrearEmpleadoForm
    success_url = reverse_lazy("lista_empleados")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class EditarEmpleado(FormView):
    template_name = "empleados/editar_empleado.html"
    form_class = EditarEmpleadoForm
    success_url = reverse_lazy("lista_empleados")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class EliminarEmpleado(FormView):
    template_name = "empleados/eliminar_empleado.html"
    form_class = EliminarEmpleadoForm
    success_url = reverse_lazy("lista_empleados")

    def form_valid(self, form):
        form.delete()
        return super().form_valid(form)
