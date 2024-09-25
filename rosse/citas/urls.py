from django.urls import path
from .views import ListadoCitasView, AgendarCitaView, EditarCitaView

urlpatterns = [
    path("listado-citas/", ListadoCitasView.as_view(), name="listado_citas"),
    path("agendar-cita/", AgendarCitaView.as_view(), name="agendar_cita"),
    path("editar-cita/<int:pk>/", EditarCitaView.as_view(), name="editar_cita"),
]
