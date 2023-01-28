from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView)
from django.shortcuts import render, redirect

from .models import Post
from .forms import PostForm


class CreatePost(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'create_post.html'
    success_url = 'posts'

    def create_post(self):
        form = PostForm(self.request.POST)
        form.save()
        return redirect('posts')


def index(request):
    return render(request, 'index.html')


def posts(request):
    post = Post.objects.order_by('-id')
    return render(request, 'posts.html', {'title': 'Новостной портал - Статьи', 'post': post})
