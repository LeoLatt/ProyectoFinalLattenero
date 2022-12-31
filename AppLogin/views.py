from django.shortcuts import render
from AppLogin.forms import CrearUsuario, UserEditForm, AvatarForm
from .models import Avatar
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def inicio(request):
    if request.user.is_authenticated:
        lista=Avatar.objects.filter(user=request.user)

    return render (request, "inicio.html", {"imagen":obtenerAvatar(request)})



def obtenerAvatar(request):
    if request.user.is_authenticated:
        lista=Avatar.objects.filter(user=request.user)
        if len(lista)!=0:
            imagen=lista[0].imagen.url
        else:
            imagen="/media/avatares/avatarpordefecto.jpg"
        return imagen


def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)#ademas del post, como trae archivos (yo se que trae archivos xq conozco el form, tengo q usar request.files)
        if form.is_valid():
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)!=0:
                avatarViejo[0].delete()
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatar.save()
            return render(request, "inicio.html", {"mensaje":"Avatar agregado correctamente", "imagen":obtenerAvatar(request)})
        else:
            return render(request, "AgregarAvatar.html", {"formulario": form, "usuario": request.user, "imagen":obtenerAvatar(request)})
    else:
        form=AvatarForm()
        return render(request , "AgregarAvatar.html", {"formulario": form, "usuario": request.user, "imagen":obtenerAvatar(request)})




def register(request):
    if request.method=="POST":
        form=CrearUsuario(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            form.save()
            #aca se podria loguear el usuario, con authenticate y login... pero no lo hago
            return render(request, "inicio.html", {"mensaje":f"Usuario {username} creado correctamente", "imagen":obtenerAvatar(request)})
        else:
            return render(request, "register.html", {"form":form, "mensaje":"Error al crear el usuario", "imagen":obtenerAvatar(request)})
        
    else:
        form=CrearUsuario()
    return render(request, "register.html", {"form":form, "imagen":obtenerAvatar(request)})


def logueo(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=form.cleaned_data.get("username")
            clave=form.cleaned_data.get("password")
            usuario=authenticate(username=usu, password=clave)#trae un usuario de la base, que tenga ese usuario y ese pass, si existe, lo trae y si no None
            print(usuario)
            if usuario is not None:    
                login(request, usuario)
                return render(request, 'inicio.html', {'mensaje':f"Bienvenido {usuario}", "imagen":obtenerAvatar(request)})
            else:
                return render(request, 'login.html', {'mensaje':"Usuario o contraseña incorrectos", 'form':form, "imagen":obtenerAvatar(request)})

        else:
            return render(request, 'login.html', {'mensaje':"Usuario o contraseña incorrectos", 'form':form, "imagen":obtenerAvatar(request)})

    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form":form, "imagen":obtenerAvatar(request)})

@login_required
def editarPerfil(request):
    usuario=request.user
    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data

            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.email=info["email"]
            usuario.set_password(info["password1"])
            usuario.set_password(info["password2"])
            
            usuario.save()
            return render(request, "inicio.html", {"mensaje":"Perfil editado correctamente", "imagen":obtenerAvatar(request)})
        else:
            return render(request, "editarUsuario.html", {"form":form, "nombreusuario":usuario.username, "mensaje":"Error al editar el perfil", "imagen":obtenerAvatar(request)})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "editarUsuario.html", {"form":form, "nombreusuario":usuario.username, "imagen":obtenerAvatar(request)})


def logOut(request):
    logout(request)
    return render(request, "logout.html", {"mensaje": "Ha cerrado sesion exitosamente"})


def about(request):
    
    return render(request, "about.html", {"imagen": obtenerAvatar(request)})