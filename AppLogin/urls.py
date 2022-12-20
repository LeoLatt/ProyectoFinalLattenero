from django.urls import path
from AppLogin.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView


urlpatterns = [
    
    path("", inicio,name='inicio'),

    path("register/",register,name='register'), #para el registro usuario
    path("login/", logueo, name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("editarperfil/", editarPerfil, name='editarPerfil'), # me muestra el formulario para editar (template 'editar perfil') y tmb llama a la funcion editarPerfil
    path("agregarAvatar/", agregarAvatar, name="agregarAvatar")
]#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)