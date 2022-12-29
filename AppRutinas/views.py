from django.shortcuts import render
from.models import Posteo
from.forms import PostForm
from AppLogin.views import obtenerAvatar
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import date
# Create your views here.


def inicio(request):
    if request.user.is_authenticated:
        posteos = Posteo.objects.all().order_by('-id')[:4] # Consulta por id, y limita a 4 de mayor a menor (ORDER BY id DESC en SQL) (LIMIT 4)
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
        return render(request, "inicio.html", {"post1": post1, "post2": post2, "post3": post3, "post4": post4}, {"imagen": obtenerAvatar(request)})


    return render (request, "inicio.html") #Llama al html Fitness de template


#@login_required
def posteoForm(request): #add_post

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form=form.cleaned_data
            post=Posteo(titulo=form["titulo"], imagen=form["imagen"], cuerpo=form["cuerpo"], fecha = date.today(),subtitulo=form["subtitulo"], autor=form["autor"])
            post.save()
            return render(request, 'inicio.html', {'form':form, "mensaje": "El posteo fue subido correctamente!", "imagen": obtenerAvatar(request)})
        else:
            return render(request, "posteoForm.html", {"form" : PostForm(), "mensaje": "Error: Poste de nuevo por favor"})    
    else:

        form = PostForm()
        return render(request, 'posteoForm.html', {'form':form, "imagen": obtenerAvatar(request)})


def post(request, id):
    lectura_publicacion = Posteo.objects.get(id = id)
    return render(request, "post.html", {"lectura_publicacion" : lectura_publicacion, "imagen": obtenerAvatar(request)})

def posteos(request):
    posteos = Posteo.objects.all().order_by('-id') # Consulta por id, de mayor a menor (ORDER BY id DESC en SQL)
    return render(request, "posteos.html", {"posteos": posteos, "imagen": obtenerAvatar(request)}) 

#@login_required
def eliminarPost(request, id):
    post=Posteo.objects.get(id=id)
    post.delete()
    posteos=Posteo.objects.all().order_by('-id')
    return render(request, "posteos.html", {"mensaje":"Post eliminado correctamente", "posteos":posteos, "imagen": obtenerAvatar(request)})

#@login_required   
def editarPosteos(request, id):
    posteo=Posteo.objects.get(id=id)
    if request.method=="POST":
        form=PostForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            informacion= form.cleaned_data
            image = informacion["imagen"]
            if str(type(image)) == "<class 'NoneType'>":      # Si el campo de imagen no tiene cambios, simplemente no actualiza el objeto de la db.
                pass
            else:                                                   # Si entra al else, es por que se le cargo una imagen.
                posteo.imagen = informacion["imagen"]

            posteo.titulo= informacion["titulo"]
            posteo.subtitulo= informacion["subtitulo"]
            posteo.cuerpo= informacion["cuerpo"]
            posteo.autor= informacion["autor"]
            posteo.fecha= informacion["fecha"]

            posteo.save() # guardo el posteo con los datos nuevos
            print(posteo)
            posteos=Posteo.objects.all().order_by('-id') #llamo a todos los posteos para q los muestre
            return render (request, "posteos.html", {"mensaje": "POSTEO EDITADO CORRECTAMENTE!!", "posteos":posteos, "imagen": obtenerAvatar(request)})
    else:
        form= PostForm(initial={"titulo":posteo.titulo, "subtitulo":posteo.subtitulo, "imagen":posteo.imagen, "cuerpo":posteo.cuerpo, "autor":posteo.autor, "fecha":posteo.fecha})
        #manda los datos iniciales del profe q se van a modificar, por get, cuando pones la url en la pagina
    return render(request, "editarPosteos.html", {"form":form, "posteo":posteo, "imagen": obtenerAvatar(request)})
