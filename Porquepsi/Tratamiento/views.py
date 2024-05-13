from django.shortcuts import render

from . import models

def index(request):
    consulta = models.TipoDeConsulta.objects.all()
    contexto = {"tipos" : consulta}
    return render(request, "Tratamiento/index.html", contexto)
