from django.db import models
from django.contrib.auth.models import User


class Avatar(models.Model):
    imagen=models.ImageField(upload_to='avatares')
    user=models.ForeignKey(User, on_delete=models.CASCADE) # cascade borra tmb el avatar si borran el usuario

    def __str__(self):
        return f"{self.user} - {self.imagen}"