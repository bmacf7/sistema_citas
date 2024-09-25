from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from .models import Cliente
from .forms import ClienteForm
from django.urls import reverse_lazy


class ClienteView(ListView):
    model = Cliente
    template_name = "clientes/listado_clientes.html"
    context_object_name = "clientes"


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "clientes/detalles_cliente.html"
    context_object_name = "cliente"


class AgregarClienteView(FormView):
    model = Cliente
    template_name = "clientes/agregar_cliente.html"
    context_object_name = "cliente"
    form_class = ClienteForm
    success_url = reverse_lazy("listado_clientes")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
