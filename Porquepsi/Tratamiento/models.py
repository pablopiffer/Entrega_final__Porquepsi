from django.db import models

class Institucion(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Profesional(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    nombre = models.CharField(max_length=255)
    profesional = models.ForeignKey(Profesional, on_delete=models.SET_NULL, null=True)
    institucion = models.ForeignKey(Institucion, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre

class TipoDeConsulta(models.Model):
    nombre = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    profesional = models.ForeignKey('Profesional', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


