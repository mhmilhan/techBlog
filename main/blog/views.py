from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Post

def posts_by_category(request, category_name):
    posts = Post.objects.filter(status='published', category__category_name=category_name)
    category = get_object_or_404(Category, category_name=category_name)




    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'posts_by_category.html', context)

# Create your views here.
