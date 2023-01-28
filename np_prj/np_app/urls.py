from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='about'),
    path('posts', views.posts, name='posts'),
    path('create_post', views.create_post, name='create_post'),

]
2