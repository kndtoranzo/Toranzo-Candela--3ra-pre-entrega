from django.urls import path
from inicio import views

urlpatterns = [
    path("", views.inicio),
    path("uñas/crear/<str:modelo>/<str:largo>/<str:color>", views.crear_uñas),
]
