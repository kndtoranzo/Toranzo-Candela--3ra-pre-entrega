from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as login_django
from usuarios.forms import RegistroForm, EditarPerfilF, CambiarContrasenia
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


def login(request):
    formulario = AuthenticationForm()
    
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get("username")
            contrasenia = formulario.cleaned_data.get("password")
            
            user = authenticate(request, username=usuario, password=contrasenia)
            login_django(request, user)
            
            return redirect("inicio")
    return render(request, "usuarios/iniciar_sesion.html", {"formulario": formulario})

def registro(request):
    formulario = RegistroForm()
    if request.method == "POST":
        formulario = RegistroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("login")
    return render(request, "usuarios/registro.html", {"formulario": formulario})

@login_required
def perfil(request):
    perfil = request.user
    return render(request, "usuarios/perfil.html", {"perfil": perfil})
@login_required
def EditarPerfil(request):
    formulario = EditarPerfilF(instance= request.user)
    if request.method == "POST":
        formulario = EditarPerfilF(request.POST, instance= request.user)
        if formulario.is_valid():
            datosextra = request.user.datosextra
            datosextra.avatar =formulario.cleaned_data.get("avatar")
            datosextra.save()
            
            formulario.save()
            return redirect(EditarPerfil)
    return render(request, "usuarios/editar_perfil.html", {"formulario": formulario})
   
class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = "usuarios/cambiar_contrasenia.html"
    success_url = reverse_lazy("perfil")
