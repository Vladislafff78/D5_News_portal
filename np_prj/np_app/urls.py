from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='about'),
    path('posts', views.posts, name='posts'),
    path('create_post', views.CreatePost.as_view(), name='create_post'),

    ]

