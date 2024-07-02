from django.urls import path
from inicio import views

urlpatterns = [
    path("", views.inicio, name= "inicio"),
    path("unias/", views.crear_uñas, name='crear_uñas'),
    path("unias/lista", views.unias, name='unias'),
    

]
