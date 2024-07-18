from django.urls import path
from django.contrib.auth.views import LogoutView
from usuarios import views

urlpatterns = [
    path("logout/", LogoutView.as_view(template_name="usuarios/cerrar_sesion.html"), name="logout"),
    path("login/", views.login, name="login"),
    path("registro/", views.registro, name="registro"),
    path('perfil/', views.perfil, name='perfil'),
    path('editar_perfil/<int:id>/', views.EditarPerfil, name='editar_perfil'),
    path('cambiar_contrasenia/<int:id>/', views.CambiarContrasenia, name='cambiar_contrasenia'),
]
