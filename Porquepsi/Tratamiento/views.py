from django.shortcuts import redirect, render

from Tratamiento.forms import TratamientopacienteForm
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

def paciente_create(request):
    if request.method == "POST":
        form = TratamientopacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Tratamiento:lista_pacientes")
    else:  # GET
        form = TratamientopacienteForm()
    return render(request, "Tratamiento/paciente_form.html", {"form": form})


def paciente_detalles(request, pk: int):
    consulta = Paciente.objects.get(id=pk)
    contexto = {"Paciente": consulta}
    return render(request, "Tratamiento/paciente_detalles.html", contexto)


def paciente_update(request, pk: int):
    consulta = Paciente.objects.get(id=pk)
    if request.method == "POST":
        form = TratamientopacienteForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("Tratamiento:lista_pacientes")
    else:  # GET
        form = TratamientopacienteForm(instance=consulta)
    return render(request, "Tratamiento/paciente_form.html", {"form": form})


def paciente_delete(request, pk: int):
    consulta = Paciente.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("Tratamiento:lista_pacientes")
    return render(request, "Tratamiento/paciente_confirm_delete.html", {"object": consulta})