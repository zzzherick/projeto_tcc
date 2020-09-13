from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'author', 'status']
        ###fields = ['title', 'slug', 'body', """image""" 'author', 'status']