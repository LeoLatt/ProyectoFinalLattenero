from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from AppLogin.views import obtenerAvatar
from AppLogin.models import *
from .models import *
from django.http import HttpResponse
from Chat.forms import *

from django.utils.functional import SimpleLazyObject

# Create your views here.


def mensajeFormulario(request):
    usuario=request.user 
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        
        if form.is_valid():
            form = form.cleaned_data
            print(form)

            paraquien = form['receiver']
            textoMensaje = form['mensaje']
            
            mensaje1 = Mensaje(enviar=(usuario), recibir = (paraquien), mensaje=textoMensaje, leido = False)
            mensaje1.save()
            return render(request, 'mensajeFormulario.html', {"form": form, "alerta": "Mensaje enviado correctamente", "imagen": obtenerAvatar(request)} )
        else:
            return render(request, 'home.html', {"alerta": "Error al enviar el mensaje", "imagen": obtenerAvatar(request)} )
    else:
        form = MensajeForm()
       
    return render(request, 'mensajeFormulario.html', {"form": form, "imagen": obtenerAvatar(request)} )

def MensajeRecibido(request):
    usuario = request.user
    herram = Mensaje.objects.filter(recibir = usuario)
    for mensaje in herram:
        mensaje.leido = True
        mensaje.save()
    print(herram)
    
    return render(request, "MensajeRecibido.html", {"mensajes": herram, "imagen": obtenerAvatar(request)})

def MensajeEnviado(request):
    usuario = request.user
    herram = Mensaje.objects.filter(enviar = usuario)
    print(herram)
    
    return render(request, "MensajeEnviado.html", {"mensajes": herram, "imagen": obtenerAvatar(request)})

def buscarMensaje(request):
    pass

def mensajeUsuarios(request):
   
    if request.method == "GET":
        return render(request, 'mensajeUsuarios.html',
                      {'users': User.objects.exclude(username=request.user.username), "imagen": obtenerAvatar(request)})


