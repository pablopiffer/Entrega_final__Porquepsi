from django.urls import path
from . import views

app_name = 'notificaciones'

urlpatterns = [
    path('crear_recordatorio/', views.crear_recordatorio, name='crear_recordatorio'),
    path('lista_recordatorios/', views.lista_recordatorios, name='lista_recordatorios'),
    path('lista_notificaciones/', views.lista_notificaciones, name='lista_notificaciones'),
]
