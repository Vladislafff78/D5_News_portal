from .models import Post
from django.forms import ModelForm, TextInput, Textarea


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["post_title", "post_text", "post_author"]
        widgets = {
            "post_title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название статьи'
            }),
            "post_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст статьи'
            }),
            "post_author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя Автора'
            })
        }
