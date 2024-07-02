from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as login_django
from usuarios.forms import Registro


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