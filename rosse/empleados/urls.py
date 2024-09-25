from django.urls import path
from .views import ListaEmpleados, CrearEmpleado, EditarEmpleado, EliminarEmpleado

urlpatterns = [
    path("lista-empleados/", ListaEmpleados.as_view(), name="lista_empleados"),
    path("crear-empleado/", CrearEmpleado.as_view(), name="crear_empleado"),
    path("editar-empleado/<int:pk>/", EditarEmpleado.as_view(), name="editar_empleado"),
    path(
        "eliminar-empleado/<int:pk>/",
        EliminarEmpleado.as_view(),
        name="eliminar_empleado",
    ),
]
