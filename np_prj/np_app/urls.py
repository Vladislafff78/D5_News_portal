from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='about'),
    path('authors', views.authors, name='authors'),
    path('posts', views.posts, name='posts'),
    path('create_post', views.create_post, name='create_post')
]
