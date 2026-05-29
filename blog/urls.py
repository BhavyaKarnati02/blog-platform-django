from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path(
        'search/',
        views.search_posts,
        name='search_posts'
    ),

    path(
        'create/',
        views.create_post,
        name='create_post'
    ),

    path(
        'post/<int:post_id>/',
        views.post_detail,
        name='post_detail'
    ),

    path(
        'like/<int:post_id>/',
        views.like_post,
        name='like_post'
    ),

    path(
        'edit/<int:post_id>/',
        views.edit_post,
        name='edit_post'
    ),

    path(
        'delete/<int:post_id>/',
        views.delete_post,
        name='delete_post'
    ),
]