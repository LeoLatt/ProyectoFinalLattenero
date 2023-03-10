from django.shortcuts import render
from.models import Posteo
from.forms import PostForm
from AppLogin.views import obtenerAvatar
from AppLogin.models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import date
# Create your views here.


def inicioRut(request):
    if request.user.is_authenticated:
        posteos = Posteo.objects.all().order_by('-id')[:4] 
        if len(posteos) == 0:
            post1 = Posteo.objects.none()
            post2 = Posteo.objects.none()
            post3 = Posteo.objects.none()
            post4 = Posteo.objects.none()
        elif len(posteos) == 1:
            post1 = posteos[0]
            post2 = Posteo.objects.none()
            post3 = Posteo.objects.none()
            post4 = Posteo.objects.none()
        elif len(posteos) == 2:
            post1 = posteos[0]
            post2 = posteos[1]
            post3 = Posteo.objects.none()
            post4 = Posteo.objects.none()
        elif len(posteos) == 3:
            post1 = posteos[0]
            post2 = posteos[1]
            post3 = posteos[2]
            post4 = Posteo.objects.none()
        else:     
            post1 = posteos[0]
            post2 = posteos[1]
            post3 = posteos[2]
            post4 = posteos[3]
        return render(request, "inicioRut.html", {"post1": post1, "post2": post2, "post3": post3, "post4": post4, "imagen": obtenerAvatar(request)})


    return render (request, "inicioRut.html", {"imagen": obtenerAvatar(request)}) 


@login_required
def posteoForm(request): 

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form=form.cleaned_data
            post=Posteo(titulo=form["titulo"], imagen=form["imagen"], cuerpo=form["cuerpo"], fecha = date.today(),subtitulo=form["subtitulo"], autor=form["autor"])
            if post.imagen:                  
                post.save()
                return render(request, 'inicio.html', {'form':form, "mensaje": "El posteo fue subido correctamente!", "imagen": obtenerAvatar(request)})
            else: 
                return render(request, "posteoForm.html", {"form" : PostForm(request.POST, request.FILES), "mensaje": "Error: Debe ingresar una imagen"})      
        else:
            return render(request, "posteoForm.html", {"form" : PostForm(), "mensaje": "Error: Debe ingresar una imagen"})    
    else:

        form = PostForm()
        return render(request, 'posteoForm.html', {'form':form, "imagen": obtenerAvatar(request)})

@login_required
def post(request, id):
    publicacion = Posteo.objects.get(id = id)
    return render(request, "post.html", {"publicacion" : publicacion, "mensaje": "Visualizacion de los detalles del Posteo", "imagen": obtenerAvatar(request)})

@login_required
def posteos(request):
    posteos = Posteo.objects.all().order_by('-id') 
    return render(request, "posteos.html", {"posteos": posteos, "imagen": obtenerAvatar(request)}) 

@login_required
def eliminarPost(request, id):
    username=request.user.get_username()
    post=Posteo.objects.get(id=id)
    if username==post.autor or request.user.is_superuser:
        post.delete()
        posteos=Posteo.objects.all().order_by('-id')
        return render(request, "mensajes.html", {"mensaje":"Post eliminado correctamente", "posteos":posteos, "imagen": obtenerAvatar(request)})
    else:
        return render(request, "mensajes.html", {"mensaje": "Solo puede Borrar sus publicaciones!", "imagen": obtenerAvatar(request)})

@login_required   
def editarPosteos(request, id):
    username=request.user.get_username()
    posteo=Posteo.objects.get(id=id)
    if username==posteo.autor or request.user.is_superuser:
        if request.method=="POST":
            form=PostForm(request.POST, request.FILES)
            print(form)
            if form.is_valid():
                informacion= form.cleaned_data
                image = informacion["imagen"]
                if str(type(image)) == "<class 'NoneType'>":      
                    pass
                else:                                                   
                    posteo.imagen = informacion["imagen"]

                posteo.titulo= informacion["titulo"]
                posteo.subtitulo= informacion["subtitulo"]
                posteo.cuerpo= informacion["cuerpo"]
                posteo.autor= informacion["autor"]
                posteo.fecha= informacion["fecha"]

                posteo.save() 
                print(posteo)
                posteos=Posteo.objects.all().order_by('-id') 
                return render (request, "mensajes.html", {"mensaje": "POSTEO EDITADO CORRECTAMENTE!!", "posteos":posteos, "imagen": obtenerAvatar(request)})
        else:
            form= PostForm(initial={"titulo":posteo.titulo, "subtitulo":posteo.subtitulo, "imagen":posteo.imagen, "cuerpo":posteo.cuerpo, "autor":posteo.autor, "fecha":posteo.fecha})
            
        return render(request, "editarPosteos.html", {"form":form, "posteo":posteo, "imagen": obtenerAvatar(request)})
    else:
        return render(request, "mensajes.html", {"mensaje": "Solo puede editar sus publicaciones!", "imagen": obtenerAvatar(request)})
