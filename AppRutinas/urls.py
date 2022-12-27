from django.urls import path
from AppRutinas.views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    path("", inicio, name='inicio'),
    #path("index/", index, name='index'),
    path("posteoForm/", posteoForm, name='posteoForm'),
    path("post/<id>", post, name = "post"),
    path("posteos", posteos, name= "posteos"),
    path("eliminarpost/<id>", eliminarPost, name = "eliminarPost"),
    path("editarPosteos/<id>", editarPosteos, name="editarPosteos"),

]