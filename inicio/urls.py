from django.urls import path
from inicio import views

urlpatterns = [
    path("", views.inicio, name= "inicio"),
    path("unias/", views.crear_uñas, name='crear_uñas'),
    path("unias/lista/", views.unias, name='unias'),
    path("unias/eliminar/<int:id>/", views.eliminar_unia, name='eliminar_unia'),
    path('unias/editar/<int:id>/', views.editar_unia, name='editar_unia'),
    path('unias/ver/<int:id>/', views.ver_unia, name='ver_unia'),
]