from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as login_django
from usuarios.forms import Registro, EditarPerfilF, CambiarContrasenia
from usuarios.models import Registro
from django.contrib.auth.decorators import login_required


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
    formulario = Registro()
    if request.method == "POST":
        formulario = Registro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("login")
    return render(request, "usuarios/registro.html", {"formulario": formulario})
@login_required
def perfil(request):
    perfil = request.user
    return render(request, "usuarios/perfil.html", {"perfil": perfil})

def EditarPerfil(request, id):
    perfil = get_object_or_404(Registro, id=id)
    formulario = EditarPerfilF(initial={"username": perfil.username, "email": perfil.email})
    
    if request.method == "POST":
        formulario = EditarPerfilF(request.POST, instance=perfil)
        if formulario.is_valid():
            formulario.save()
            return redirect("perfil_default")
    
    return render(request, "usuarios/editar_perfil.html", {"formulario": formulario, "perfil": perfil})
    
def CambiarContrasenia(request):
    ...    
