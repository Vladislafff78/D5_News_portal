from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def index(request):
    return render(request, 'index.html')


def posts(request):
    post = Post.objects.order_by('-id')
    return render(request, 'posts.html', {'title': 'Новостной портал - Статьи', 'post': post})


def authors(request):
    return render(request, 'authors.html')


def create_post(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
        else:
            error = 'Что то пошло не так'

    form = PostForm()
    context = {
        'form': form,
        'error': error
    }

    return render(request, 'create_post.html', context)
