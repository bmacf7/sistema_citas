from django.urls import path
from .views import CrearServicio, EditarServicio, ListadoServicios

urlpatterns = [
    path("listado-servicios/", ListadoServicios.as_view(), name="listado_servicios"),
    path("crear-servicio/", CrearServicio.as_view(), name="crear_servicio"),
    path("editar-servicio/<int:pk>", EditarServicio.as_view(), name="editar_servicio"),
]
