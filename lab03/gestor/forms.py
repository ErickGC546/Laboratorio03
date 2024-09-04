from django import forms
from .models import Propietario, Vehiculo, Registro

class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = ['nombre', 'numero_apartamento', 'telefono', 'email']

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['matricula', 'marca', 'modelo', 'color', 'propietario']

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['vehiculo']