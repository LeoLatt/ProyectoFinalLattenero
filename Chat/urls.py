from django.urls import path, include
from . import views
from django.contrib import admin
from django.urls import path
from Chat.views import *
# se importa el logout directamente al url
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("", views.home, name = "home"),
    path("mensajeFormulario", mensajeFormulario , name = "mensajeFormulario"),
    path("mensajeUsuarios", mensajeUsuarios , name = "mensajeUsuarios"),
    path("MensajeRecibido", MensajeRecibido , name = "MensajeRecibido"),
    path("mensajeEnviado", MensajeEnviado , name = "MensajeEnviado"),
]