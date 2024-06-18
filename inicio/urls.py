from django.urls import path
from inicio import views

urlpatterns = [
    path("", views.inicio, name= "inicio"),
    path("uñas/", views.crear_uñas, name='crear_uñas'),
    path("uñas/lista", views.unias, name='unias'),

]
