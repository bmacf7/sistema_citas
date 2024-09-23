from django.urls import path

urlpatterns = [
    path("listado-clientes/", ClientesView.as_view(), name="clientes"),
]
