from django.shortcuts import redirect, render

#from producto.forms import ProductoCategoriaForm
from .models import Paciente


def index(request):
    return render(request, "Tratamiento/index.html")


def lista_pacientes(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        print(busqueda)
        consulta = Paciente.objects.filter(nombre__icontains=busqueda)
    else:
        consulta = Paciente.objects.all()
    contexto = {"Paciente": consulta}
    return render(request, "Tratamiento/lista_pacientes.html", contexto)