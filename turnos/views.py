from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Turnos
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class TurnosListView(ListView):
    model = Turnos
    template_name = "turnos/agenda.html"
    context_object_name = "turnos"
    
class CrearTurno(CreateView):
    model = Turnos
    template_name = "turnos/crear_turno.html"
    success_url = reverse_lazy("agenda")
    fields = ["fecha", "tipo_manicura", "descripcion"]
    
class EditarTurno(LoginRequiredMixin, UpdateView):
    model = Turnos
    template_name = "turnos/editar_turno.html"
    success_url = reverse_lazy("agenda")
    fields = ["fecha", "tipo_manicura", "descripcion"]

class VerTurno(DetailView):
    model = Turnos
    template_name = "turnos/ver_turno.html" 

class EliminarTurno(LoginRequiredMixin, DeleteView):
    model = Turnos
    template_name = "turnos/eliminar_turno.html"
    success_url = reverse_lazy("agenda")   