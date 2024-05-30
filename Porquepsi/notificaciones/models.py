from django.db import models
from django.contrib.auth.models import User
from Tratamiento.models import Profesional
from datetime import datetime

class Notificacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    mensaje = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return f'Notificación para {self.usuario.username} - {self.mensaje}'

class Recordatorio(models.Model):
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    mensaje = models.TextField()
    fecha_recordatorio = models.DateTimeField()
    enviado = models.BooleanField(default=False)

    def __str__(self):
        return f'Recordatorio para {self.profesional.user.username} el {self.fecha_recordatorio}'
