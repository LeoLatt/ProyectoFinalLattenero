from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField 

from django import forms
from django.forms import ModelForm
from django.core.cache import cache
cache.clear()
from AppRutinas.models import *


# Create your models here.
class Posteo(models.Model):

    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='media', blank=True)
    cuerpo = RichTextUploadingField() # CKEditor Rich Text Field
    autor = models.CharField(max_length=255)
    fecha = models.DateTimeField(default='2023-8-1')

    def __str__(self):
        return self.titulo

