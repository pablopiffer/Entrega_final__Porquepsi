from django.contrib.auth.models import User
from django.db import models
import datetime

class Institucion(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Profesional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profesional")
    especialidad = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    institucion = models.ForeignKey(Institucion, on_delete=models.SET_NULL, null=True, blank=True)
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)
    activo = models.BooleanField(default=True)  # Campo agregado

    def __str__(self):
        return self.user.username

class Paciente(models.Model):
    nombre = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    profesional = models.ForeignKey(Profesional, on_delete=models.SET_NULL, null=True, blank=True)
    institucion = models.ForeignKey(Institucion, on_delete=models.SET_NULL, null=True, blank=True)
    numero_historia_clinica = models.CharField(max_length=100, unique=True, null=True, blank=True)
    activo = models.BooleanField(default=True) 

    def __str__(self):
        return self.nombre

class TipoDeConsulta(models.Model):
    nombre = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pagado = models.BooleanField(default=False)
    fecha = models.DateField(default=datetime.date.today)
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    duracion = models.DurationField(null=True, blank=True)

    def __str__(self):
        return self.nombre
    
from .models import Paciente, Profesional

class NotaDeSesion(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return f"Nota de sesión para {self.paciente} - {self.fecha}"

class ObjetivoDeTratamiento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return f"Objetivo de tratamiento para {self.paciente}"



