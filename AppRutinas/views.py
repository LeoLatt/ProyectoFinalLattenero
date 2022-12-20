from django.shortcuts import render
from.models import Posteo
from.forms import PostForm
from django.http import HttpResponseRedirect
# Create your views here.


def inicio(request):
    
    return render (request, "inicio.html") #Llama al html Fitness de template



def posteoForm(request):

    form = None
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:

        form = PostForm()
    return render(request, 'posteoForm.html',{'form':form})