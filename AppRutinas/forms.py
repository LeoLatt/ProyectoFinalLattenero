from django.forms import ModelForm
from.models import Posteo

class PostForm(ModelForm):
    class Meta:
        model = Posteo
        fields = ['titulo','cuerpo']