from django.urls import path
from .views import MascotaView, AgregarMascotaView

urlpatterns = [
    path("listado-mascotas/", MascotaView.as_view(), name="listado_mascotas"),
    path("agregar-mascota/", AgregarMascotaView.as_view(), name="agregar_mascota"),
    path("detalle-mascota/<int:pk>/", MascotaView.as_view(), name="detalle_mascota"),
]
