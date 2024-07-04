from django import forms


class UniaFormularioBase(forms.Form):
    modelo = forms.CharField(max_length=20)
    largo = forms.CharField(max_length=20)
    color = forms.CharField(max_length=20)
    
class crear_unias(UniaFormularioBase):
    ...

class EditarUnia(UniaFormularioBase):
    ...    
    
class buscar_unia(forms.Form):
    modelo = forms.CharField(max_length=20, required=False)