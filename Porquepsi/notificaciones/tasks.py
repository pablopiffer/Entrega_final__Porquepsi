from celery import shared_task
from .models import Recordatorio
from django.core.mail import send_mail
from django.utils import timezone

@shared_task
def enviar_recordatorios():
    recordatorios = Recordatorio.objects.filter(enviado=False, fecha_recordatorio__lte=timezone.now())
    for recordatorio in recordatorios:
        send_mail(
            'Recordatorio de Consulta',
            recordatorio.mensaje,
            'from@example.com',
            [recordatorio.profesional.user.email],
            fail_silently=False,
        )
        recordatorio.enviado = True
        recordatorio.save()
