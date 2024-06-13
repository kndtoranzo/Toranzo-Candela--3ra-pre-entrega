from django.urls import path
from inicio import views

urlpatterns = [
    path("", views.inicio, name= "inicio"),
    path("uñas/<modelo>/<largo>/<color>", views.crear_uñas, name='crear_uñas'),
]
