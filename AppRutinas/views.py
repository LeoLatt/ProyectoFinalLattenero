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
        blogs = Posteo.objects.all().order_by('-id')[:4] # Consulta por id, y limita a 4 de mayor a menor (ORDER BY id DESC en SQL) (LIMIT 4)
        if len(blogs) == 0:
            blog_1 = Posteo.objects.none()
            blog_2 = Posteo.objects.none()
            blog_3 = Posteo.objects.none()
            blog_4 = Posteo.objects.none()
        elif len(blogs) == 1:
            blog_1 = blogs[0]
            blog_2 = Posteo.objects.none()
            blog_3 = Posteo.objects.none()
            blog_4 = Posteo.objects.none()
        elif len(blogs) == 2:
            blog_1 = blogs[0]
            blog_2 = blogs[1]
            blog_3 = Posteo.objects.none()
            blog_4 = Posteo.objects.none()
        elif len(blogs) == 3:
            blog_1 = blogs[0]
            blog_2 = blogs[1]
            blog_3 = blogs[2]
            blog_4 = Post.objects.none()
        else:     
            blog_1 = blogs[0]
            blog_2 = blogs[1]
            blog_3 = blogs[2]
            blog_4 = blogs[3]
        return render(request, "inicio.html", {"blog_1": blog_1, "blog_2": blog_2, "blog_3": blog_3, "blog_4": blog_4}, {"imagen": obtenerAvatar(request)})


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
            return render(request, 'posteoForm.html', {'form':form, "mensaje_publicacion": "El posteo fue subido correctamente!", "imagen": obtenerAvatar(request)})
    else:

        form = PostForm()
    return render(request, 'posteoForm.html', {'form':form, "imagen": obtenerAvatar(request)})


def post(request, id):
    lectura_publicacion = Posteo.objects.get(id = id)
    return render(request, "post.html", {"lectura_publicacion" : lectura_publicacion, "imagen": obtenerAvatar(request)})

def posteos(request):
    blogs = Posteo.objects.all().order_by('-id') # Consulta por id, de mayor a menor (ORDER BY id DESC en SQL)
    return render(request, "posteos.html", {"blogs": blogs, "imagen": obtenerAvatar(request)}) 

