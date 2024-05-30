from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Notificacion, Recordatorio
from .forms import RecordatorioForm
from django.utils import timezone

@login_required
def crear_recordatorio(request):
    if request.method == 'POST':
        form = RecordatorioForm(request.POST)
        if form.is_valid():
            recordatorio = form.save(commit=False)
            if hasattr(request.user, 'profesional'):
                recordatorio.profesional = request.user.profesional
                recordatorio.save()
                return redirect('notificaciones:lista_recordatorios')
            else:
                # Maneja el caso donde el usuario no tiene un perfil de profesional
                # Puedes redirigir a otra página o mostrar un mensaje de error
                return render(request, 'no_profesional.html')
    else:
        form = RecordatorioForm()
    return render(request, 'notificaciones/crear_recordatorio.html', {'form': form})

@login_required
def lista_recordatorios(request):
    recordatorios = Recordatorio.objects.filter(profesional=request.user.profesional)
    return render(request, 'notificaciones/lista_recordatorios.html', {'recordatorios': recordatorios})

@login_required
def lista_notificaciones(request):
    notificaciones = Notificacion.objects.filter(usuario=request.user)
    return render(request, 'notificaciones/lista_notificaciones.html', {'notificaciones': notificaciones})
