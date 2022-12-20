from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField 

# Create your models here.
class Posteo(models.Model):

    titulo = models.CharField(max_length=255)
    #body = models.TextField() 
    cuerpo = RichTextUploadingField() # CKEditor Rich Text Field

    def __str__(self):
        return self.titulo

