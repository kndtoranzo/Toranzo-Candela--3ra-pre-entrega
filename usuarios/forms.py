from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="contrasenia", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirmar contrasenia", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields =["username", "email", "password1", "password2"]
        help_texts = {key: "" for key in fields}

class EditarPerfilF(UserChangeForm):
    password = None
    email = forms.EmailField()
    username = forms.CharField(label="nombre")
    last_name = forms.CharField(label="apellido")
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields =["email", "username", "last_name", "avatar"]

class CambiarContrasenia(forms.Form):
    new_password = forms.CharField(label="Nueva contraseña", widget=forms.PasswordInput)