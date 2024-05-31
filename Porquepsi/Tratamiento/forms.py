from django import forms

from . import models
from .models import NotaDeSesion, ObjetivoDeTratamiento


class TratamientopacienteForm(forms.ModelForm):
    class Meta:
        model = models.Paciente
        fields = "__all__"           
                    


class InstitucionForm(forms.ModelForm):
    class Meta:
        model = models.Institucion
        fields = "__all__"

class NotaDeSesionForm(forms.ModelForm):
    class Meta:
        model = NotaDeSesion
        fields = ['paciente', 'contenido', 'fecha']

class ObjetivoDeTratamientoForm(forms.ModelForm):
    class Meta:
        model = ObjetivoDeTratamiento
        fields = ['paciente', 'descripcion', 'fecha']
