from django import forms


class crear_unias(forms.Form):
    Estilo = forms.CharField(max_length=20)
    Largo = forms.CharField(max_length=20)
    Color = forms.CharField(max_length=20)