from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from django.contrib.auth.models import login
# Create your models here.


class CrearUsuario(UserCreationForm):
    nombre= models.CharField(max_length=50)
    email= models.EmailField()
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)
        
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
        help_text={k:"" for k in fields} #para cada uno de los campos del formulario, le asigna un valor vacio

