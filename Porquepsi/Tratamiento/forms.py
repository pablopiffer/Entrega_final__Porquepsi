from django import forms

from . import models


class TratamientopacienteForm(forms.ModelForm):
    class Meta:
        model = models.Paciente
        fields = ["nombre", "institucion"]