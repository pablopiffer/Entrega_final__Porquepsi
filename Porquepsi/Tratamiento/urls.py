from django.urls import path

from . import views

app_name = "Tratamiento"

urlpatterns = [
    path("", views.index, name="index"),
] 