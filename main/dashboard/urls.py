from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('categories/', views.categories, name='categories'),
    path('categories/add/', views.add_category, name='add_category'),
    path('categories/edit/<str:category_name>/', views.edit_category, name='edit_category'),
    path('categories/delete/<str:category_name>/', views.delete_category, name='delete_category'),
    # Posts
    path('posts/', views.posts, name='posts'),
    path('posts/add/', views.add_posts, name='add_posts'),
    path('posts/edit/<str:category_name>/<slug:slug>/', views.edit_post, name='edit_post'),
    path('posts/delete/<str:category_name>/<slug:slug>/', views.delete_post, name='delete_post'),
    # Social Media Links
    path('social-media/', views.social_media, name='social_media'),
    path('social-media/add/', views.add_social_media, name='add_social_media'),
    path('social-media/edit/<str:platform>/', views.edit_social_media, name='edit_social_media'),
    path('social-media/delete/<str:platform>/', views.delete_social_media, name='delete_social_media'),
]
