from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.users, name='users'),
    path('users/add/', views.add_user, name='add_user'),
    path('users/edit/<str:username>/', views.edit_user, name='edit_user'),
    path('users/delete/<str:username>/', views.delete_user, name='delete_user'),
]

