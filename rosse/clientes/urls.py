from django.urls import path
from .views import ClienteView, ClienteDetailView, AgregarClienteView

urlpatterns = [
    path("listado-clientes/", ClienteView.as_view(), name="listado_clientes"),
    path(
        "detalles-cliente/<int:pk>/",
        ClienteDetailView.as_view(),
        name="detalles_cliente",
    ),
    path("agregar-cliente/", AgregarClienteView.as_view(), name="agregar_cliente"),
]
