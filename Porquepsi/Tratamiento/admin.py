from django.contrib import admin

from . import models

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_nacimiento', 'direccion', 'telefono', 'email', 'numero_historia_clinica')
    list_display_links = ('nombre',) 
    list_filter = ('profesional', 'institucion') 
    search_fields = ('nombre', 'numero_historia_clinica')
    date_hierarchy = 'fecha_nacimiento'  


admin.site.register(models.Profesional)
admin.site.register(models.Paciente, PacienteAdmin)
admin.site.register(models.TipoDeConsulta)
admin.site.register(models.Institucion)
#admin.site.register(models.NotaDeSesion)
#admin.site.register(models.ObjetivoDeTratamiento)
