from django.shortcuts import render
from AppLogin.registroForm import CrearUsuario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required 
# Create your views here.

def inicio(request):
    
    return render (request, "inicio.html")


def register(request):
    if request.method=="POST":
        form=CrearUsuario(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            form.save()
            #aca se podria loguear el usuario, con authenticate y login... pero no lo hago
            return render(request, "inicio.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "register.html", {"form":form, "mensaje":"Error al crear el usuario"})
        
    else:
        form=CrearUsuario()
    return render(request, "register.html", {"form":form})


def login(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=form.cleaned_data.get("username")
            clave=form.cleaned_data.get("password")
            usuario=authenticate(username=usu, password=clave)#trae un usuario de la base, que tenga ese usuario y ese pass, si existe, lo trae y si no None

            if usuario is not None:    
                login(request, usuario)
                return render(request, 'inicio.html', {'mensaje':f"Bienvenido {usuario}" })
            else:
                return render(request, 'login.html', {'mensaje':"Usuario o contraseña incorrectos", 'form':form})

        else:
            return render(request, 'login.html', {'mensaje':"Usuario o contraseña incorrectos", 'form':form})

    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form":form})
