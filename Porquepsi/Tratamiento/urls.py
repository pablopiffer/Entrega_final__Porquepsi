from django.urls import path

from Tratamiento.views import (
    index,
    lista_pacientes
)

app_name = "Tratamiento"

urlpatterns = [
    path("", index, name="index"),
    path("Tratamiento/lista_pacientes", lista_pacientes, name="lista_pacientes")
] 