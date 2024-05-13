from django.contrib import admin

from . import models

admin.site.register(models.Profesional)
admin.site.register(models.Paciente)
admin.site.register(models.TipoDeConsulta)
admin.site.register(models.Institucion)