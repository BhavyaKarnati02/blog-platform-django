from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('create/', views.create_post, name='create_post'),

    path('post/<int:post_id>/', views.post_detail, name='post_detail'),

    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),

    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
]