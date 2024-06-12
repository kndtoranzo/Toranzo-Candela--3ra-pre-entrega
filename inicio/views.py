from django.shortcuts import render
from inicio.models import manicura

def inicio(request):
    return render(request, "inicio/inicio.html")

def crear_uñas(request,modelo, largo, color ):
    unias = manicura(modelo=modelo, largo=largo, color=color)
    unias.save()
    return render(request, "uñas_templates/creacion.html", {"unias": unias})