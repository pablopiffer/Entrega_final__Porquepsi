from django.urls import path

from Tratamiento.views import (
    PacienteList,
    PacienteCreate,
    PacienteDelete,
    PacienteDetail,
    PacienteUpdate,
    EstadisticasView,
    index,

)

app_name = "Tratamiento"

urlpatterns = [
    path("", index, name="index")
    # path("lista_pacientes/", lista_pacientes, name="lista_pacientes"),
    # path("paciente_confirm_delete/<int:pk>", paciente_delete, name="paciente_confirm_delete"),
    # path("paciente_detalles/<int:pk>", paciente_detalles, name="paciente_detalles"),
    # path("paciente_update/<int:pk>", paciente_update, name="paciente_update"),
    # path("paciente_form/", paciente_create, name="paciente_form"),
]

urlpatterns += [
    path("Tratamiento/lista_pacientes", PacienteList.as_view(), name="lista_pacientes"),
    path("Tratamiento/paciente_form/", PacienteCreate.as_view(), name="paciente_form"),
    path("Tratamiento/paciente_detalles/<int:pk>", PacienteDetail.as_view(), name="paciente_detalles"),
    path("paciente_update/<int:pk>", PacienteUpdate.as_view(), name="paciente_update"),
    path("Tratamiento/paciente_confirm_delete/<int:pk>", PacienteDelete.as_view(), name="paciente_confirm_delete"),
    path('estadisticas/', EstadisticasView.as_view(), name='estadisticas'),
]
