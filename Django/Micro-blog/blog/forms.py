from django import forms
from .models import Post
class PostForm(forms.ModelForm):
    title = forms.CharField(label='Titulo de la publicación', max_length=250)
    body = forms.CharField(label='Contenido del post', widget=forms.Textarea)
    published = forms.BooleanField(label='¿Desea publicarlo?', required=False)

    class Meta:
        model = Post
        fields = ['title', 'body', 'published']