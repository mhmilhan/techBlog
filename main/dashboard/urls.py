from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('categories/', views.categories, name='categories'),
    path('categories/add/', views.add_category, name='add_category'),
    path('categories/edit/<str:category_name>/', views.edit_category, name='edit_category'),
    path('categories/delete/<str:category_name>/', views.delete_category, name='delete_category'),
    path('posts/', views.posts, name='posts'),
    path('posts/add/', views.add_posts, name='add_posts'),
    path('posts/edit/<str:category_name>/<slug:slug>/', views.edit_post, name='edit_post'),
    path('posts/delete/<str:category_name>/<slug:slug>/', views.delete_post, name='delete_post')
]
