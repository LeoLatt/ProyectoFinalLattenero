from django.urls import path
from AppRutinas.views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    path("", inicio, name='inicio'),
    #path("index/", index, name='index'),
    path("posteoForm/", posteoForm, name='posteoForm'),

]