from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from Tratamiento.models import Profesional

class ProfesionalRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user, 'profesional'):
            Profesional.objects.create(user=request.user)
        return super().dispatch(request, *args, **kwargs)

