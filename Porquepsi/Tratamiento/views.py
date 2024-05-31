from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Count
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    TemplateView,
)

from Tratamiento.forms import TratamientopacienteForm, InstitucionForm, NotaDeSesionForm, ObjetivoDeTratamientoForm
from .models import Paciente, TipoDeConsulta, Institucion, NotaDeSesion, ObjetivoDeTratamiento
from django.db import models
from .mixins import ProfesionalRequiredMixin


def index(request):
    return render(request, "Tratamiento/index.html")


""" def lista_pacientes(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        consulta = Paciente.objects.filter(nombre__icontains=busqueda)
    else:
        consulta = Paciente.objects.all()
    contexto = {"paciente": consulta}  
    return render(request, "Tratamiento/lista_pacientes.html", contexto) """

class PacienteList(LoginRequiredMixin, ListView):
    model = Paciente
    context_object_name = "paciente"
    template_name = "Tratamiento/lista_pacientes.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = queryset.filter(nombre__icontains=busqueda)
        return queryset

# def paciente_create(request):
#     if request.method == "POST":
#         form = TratamientopacienteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("Tratamiento:lista_pacientes")
#     else:  # GET
#         form = TratamientopacienteForm()
#     return render(request, "Tratamiento/paciente_form.html", {"form": form})

class PacienteCreate(LoginRequiredMixin, CreateView):
    model = Paciente
    form_class = TratamientopacienteForm
    success_url = reverse_lazy("Tratamiento:lista_pacientes")


# def paciente_detalles(request, pk: int):
#     consulta = Paciente.objects.get(id=pk)
#     contexto = {"Paciente": consulta}
#     return render(request, "Tratamiento/paciente_detalles.html", contexto)

class PacienteDetail(LoginRequiredMixin, DetailView):
    model = Paciente
    template_name = "Tratamiento/paciente_detalles.html"


# def paciente_update(request, pk: int):
#     consulta = Paciente.objects.get(id=pk)
#     if request.method == "POST":
#         form = TratamientopacienteForm(request.POST, instance=consulta)
#         if form.is_valid():
#             form.save()
#             return redirect("Tratamiento:lista_pacientes")
#     else:  # GET
#         form = TratamientopacienteForm(instance=consulta)
#     return render(request, "Tratamiento/paciente_form.html", {"form": form})

class PacienteUpdate(LoginRequiredMixin, UpdateView):
    model = Paciente
    form_class = TratamientopacienteForm
    template_name = "paciente_form.html"
    success_url = reverse_lazy("Tratamiento:lista_pacientes")


# def paciente_delete(request, pk: int):
#     consulta = Paciente.objects.get(id=pk)
#     if request.method == "POST":
#         consulta.delete()
#         return redirect("Tratamiento:lista_pacientes")
#     return render(request, "Tratamiento/paciente_confirm_delete.html", {"object": consulta})

class PacienteDelete(LoginRequiredMixin, DeleteView):
    model = Paciente
    success_url = reverse_lazy("Tratamiento:lista_pacientes")


class EstadisticasView(LoginRequiredMixin, TemplateView):
    template_name = "Tratamiento/estadisticas.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_consultas = TipoDeConsulta.objects.count()
        consultas_por_tipo = TipoDeConsulta.objects.values('nombre').annotate(total=models.Count('id')).order_by('-total')
        consultas_por_profesional = TipoDeConsulta.objects.values('profesional__user__username').annotate(total=models.Count('id')).order_by('-total')
        consultas_por_paciente = TipoDeConsulta.objects.values('paciente__nombre').annotate(total=models.Count('id')).order_by('-total')
        
        context['total_consultas'] = total_consultas
        context['consultas_por_tipo'] = consultas_por_tipo
        context['consultas_por_profesional'] = consultas_por_profesional
        context['consultas_por_paciente'] = consultas_por_paciente
        return context





    #INSTITUCION




class InstitucionList(LoginRequiredMixin, ListView):
    model = Institucion
    context_object_name = "institucion"
    template_name = "Tratamiento/lista_institucion.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = queryset.filter(
                nombre__icontains=busqueda)
        return queryset


class InstitucionCreate(LoginRequiredMixin, CreateView):
    model = Institucion
    form_class = InstitucionForm
    success_url = reverse_lazy("Tratamiento:lista_institucion")


class InstitucionDetail(LoginRequiredMixin, DetailView):
    model = Institucion
    template_name = "Tratamiento/institucion_detalles.html"


class InstitucionUpdate(LoginRequiredMixin, UpdateView):
    model = Institucion
    form_class = InstitucionForm
    success_url = reverse_lazy("Tratamiento:lista_institucion")


class InstitucionDelete(LoginRequiredMixin, DeleteView):
    model = Institucion
    success_url = reverse_lazy("Tratamiento:lista_institucion")

class NotaDeSesionCreate(LoginRequiredMixin, CreateView):
    model = NotaDeSesion
    form_class = NotaDeSesionForm
    template_name = "Tratamiento/nota_de_sesion_form.html"
    success_url = reverse_lazy("Tratamiento:lista_pacientes")

    def form_valid(self, form):
        # Asignar el usuario actual al campo Profesional.user antes de guardar el formulario
        form.instance.profesional.user = self.request.user
        #form.instance.profesional = self.request.user.profesional
        return super().form_valid(form)

class ObjetivoDeTratamientoCreate(LoginRequiredMixin, CreateView):
    model = ObjetivoDeTratamiento
    form_class = ObjetivoDeTratamientoForm
    template_name = "Tratamiento/objetivo_de_tratamiento_form.html"
    success_url = reverse_lazy("Tratamiento:lista_pacientes")

    def form_valid(self, form):
        # Verificar si el usuario actual está autenticado
        if self.request.user.is_authenticated:
            # Verificar si el usuario tiene un perfil de profesional asociado
            if hasattr(self.request.user, 'profesional'):
                # Asignar el profesional asociado al objetivo de tratamiento
                form.instance.profesional = self.request.user
                return super().form_valid(form)
            else:
                # Si el usuario autenticado no tiene un perfil de profesional asociado,
                # redirigirlo a una página de error o mostrar un mensaje apropiado.
                return redirect("Tratamiento:lista_pacientes")
        else:
            # Si el usuario no está autenticado, redirigirlo a la página de inicio de sesión
            return redirect('login')