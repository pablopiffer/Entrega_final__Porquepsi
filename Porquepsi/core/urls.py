from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.contrib.auth.views import LogoutView

from core.views import CustomLoginView, index, register

from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    path("register/", register, name = "register")
]

urlpatterns += staticfiles_urlpatterns()