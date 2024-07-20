from django.urls import path
from django.contrib.auth.views import LogoutView
from usuarios import views

urlpatterns = [
    path("logout/", LogoutView.as_view(template_name="usuarios/cerrar_sesion.html"), name="logout"),
    path("login/", views.login, name="login"),
    path("registro/", views.registro, name="registro"),
    path('perfil/', views.perfil, name='perfil'),
    path('editar_perfil/', views.EditarPerfil, name='editar_perfil'),
    path('cambiar_contrasenia/', views.CambiarContrasenia.as_view(), name='cambiar_contrasenia'),
]
