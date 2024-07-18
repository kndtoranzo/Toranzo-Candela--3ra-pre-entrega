from django.shortcuts import render, redirect
from inicio.models import manicura
from inicio.forms import crear_unias, buscar_unia, EditarUnia

from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, "inicio/inicio.html")

def crear_uñas(request):
    print("request:", request)
    print("get:", request.GET)
    print("post:", request.POST)
    
    formulario= crear_unias()
    if request.method == "POST":
        formulario= crear_unias(request.POST)
        if formulario.is_valid():
            datos= formulario.cleaned_data
            unias= manicura(modelo=datos.get("modelo"), largo=datos.get("largo"), color=datos.get("color"))
            unias.save()
            return redirect("unias")
                   
    return render(request, "uñas_templates/creacion.html", {"formulario": formulario})

def unias(request):
    formulario = buscar_unia(request.GET)
    if formulario.is_valid():
        modelo = formulario.cleaned_data["modelo"]
        unias = manicura.objects.filter(modelo__icontains=modelo)
        unias=manicura.objects.all()
    return render(request, "inicio/unias.html", {"unias": unias, "formulario": formulario})

@login_required
def eliminar_unia(request, id):
    unia = manicura.objects.get(id=id)
    unia.delete()
    return redirect("unias")

@login_required
def editar_unia(request, id):
    unia = manicura.objects.get(id=id)
    formulario = EditarUnia(initial={"modelo": unia.modelo, "largo": unia.largo, "color": unia.color})
    
    if request.method == "POST":
        formulario = EditarUnia(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            
            unia.modelo = info["modelo"]
            unia.largo = info["largo"]
            unia.color = info["color"]
            unia.save()
            return redirect("unias")
            
    return render(request, "inicio/editar_unia.html", {"formulario": formulario, "unia": unia})

def ver_unia(request, id):
    unia = manicura.objects.get(id=id)
    return render(request, "inicio/ver_unia.html", {"unia": unia})