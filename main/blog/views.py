from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Post
from django.db.models import Q

def posts_by_category(request, category_name):
    posts = Post.objects.filter(status='published', category__category_name=category_name)
    category = get_object_or_404(Category, category_name=category_name)
    latest_posts = Post.objects.filter(is_latest=True).order_by('-updated_at')
    featured_posts = Post.objects.filter(is_featured=True).order_by('-updated_at')
    popular_posts = Post.objects.filter(is_popular=True).order_by('-updated_at')
    trending_posts = Post.objects.filter(is_trending=True).order_by('-updated_at')
    unboxing_posts = Post.objects.filter(is_unboxing=True).order_by('-updated_at')
    reviews = Post.objects.filter(is_review=True).order_by('-updated_at')
    ai_posts = Post.objects.filter(is_ai=True).order_by('-updated_at')
    invention_posts = Post.objects.filter(is_invention=True).order_by('-updated_at')
    robotics_posts = Post.objects.filter(is_robotics=True).order_by('-updated_at')
    space_posts = Post.objects.filter(is_space=True).order_by('-updated_at')

    context = {
        'category': category,
        'posts': posts,
        'latest_posts': latest_posts,
        'featured_posts': featured_posts,
        'popular_posts': popular_posts,
        'trending_posts': trending_posts,
        'unboxing_posts': unboxing_posts,
        'reviews': reviews,
        'ai_posts': ai_posts,
        'invention_posts': invention_posts,
        'robotics_posts': robotics_posts,
        'space_posts': space_posts,
    }
    return render(request, 'posts_by_category.html', context)

# Create your views here.
def post_detail(request, category_name, slug):
    post = get_object_or_404(Post, slug=slug, category__category_name=category_name, status='published')

    context = {
        'post': post,
    }
    return render(request, 'post_detail.html', context)

def search(request):
    query = request.GET.get('query')
    posts = Post.objects.filter(Q(title__icontains=query) | Q(short_description__icontains=query) | Q(content__icontains=query), status='published')
    context = {
        'posts': posts,
        'query': query,
    }

    return render(request, 'search.html', context)