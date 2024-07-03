from django import forms


class crear_unias(forms.Form):
    modelo = forms.CharField(max_length=20)
    largo = forms.CharField(max_length=20)
    color = forms.CharField(max_length=20)
    
class buscar_unia(forms.Form):
    modelo = forms.CharField(max_length=20, required=False)    