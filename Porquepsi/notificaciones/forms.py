from django import forms
from .models import Recordatorio

class RecordatorioForm(forms.ModelForm):
    class Meta:
        model = Recordatorio
        fields = ['mensaje', 'fecha_recordatorio']