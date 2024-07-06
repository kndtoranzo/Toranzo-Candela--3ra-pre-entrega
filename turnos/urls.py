from django.urls import path
from .import views

urlpatterns = [
    path("agenda/", views.TurnosListView.as_view(), name="agenda"),
    path("turnos/crear/", views.CrearTurno.as_view(), name="crear_turno"),
    path("turnos/<int:pk>/", views.VerTurno.as_view(), name="ver_turno"),
    path("turnos/editar/<int:pk>/", views.EditarTurno.as_view(), name="editar_turno"),
    path("turnos/eliminar/<int:pk>", views.EliminarTurno.as_view(), name="eliminar_turno"),

]