from django.shortcuts import render
from blog.models import Category, Post
from social.models import SocialMediaLink


def index(request):
    categories = Category.objects.all()
    posts = Post.objects.filter(status='published').order_by('-updated_at')
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
    social_media_links = SocialMediaLink.objects.all()

    context = {
        'categories': categories,
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
        'social_media_links': social_media_links,
    }

    return render(request, 'home.html', context)

