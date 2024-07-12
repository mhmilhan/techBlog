from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.utils.text import slugify

from blog.models import Category, Post
from social.models import SocialMediaLink
from .forms import CategoryForm, PostForm, SocialMediaForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    posts_count = Post.objects.all().count()

    context = {
        'category_count': category_count,
        'posts_count': posts_count,
    }
    return render(request, 'dashboard/dashboard.html', context)


def categories(request):
    return render(request, 'dashboard/categories.html')

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_category.html', context)

def edit_category(request, category_name):
    category = get_object_or_404(Category, category_name= category_name)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'dashboard/edit_category.html', context)

def delete_category(request, category_name):
    category = get_object_or_404(Category, category_name=category_name)
    category.delete()
    return redirect('categories')

def posts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'dashboard/posts.html', context)

def add_posts(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            # Ensure the slug is unique by adding the post ID to it
            post.slug = slugify(form.cleaned_data['title']) + '-' + str(post.id)
            post.save()
            return redirect('posts')
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_posts.html', context)


def edit_post(request, category_name, slug):
    post = get_object_or_404(Post, slug=slug, category__category_name=category_name)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(form.cleaned_data['title']) + '-' + str(post.id)
            post.save()
            return redirect('posts')
    else:
        form = PostForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'dashboard/edit_post.html', context)

def delete_post(request, category_name, slug):
    post = get_object_or_404(Post, slug=slug, category__category_name=category_name)
    post.delete()
    return redirect('posts')

def social_media(request):
    social_media_link = SocialMediaLink.objects.all()
    context = {
        'social_media_link': social_media_link,
    }
    return render(request, 'dashboard/social_media.html')

def add_social_media(request):
    if request.method == 'POST':
        form = SocialMediaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('social_media')
    form = SocialMediaForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_social_media.html', context)

def edit_social_media(request, platform):
    social_media_link = get_object_or_404(SocialMediaLink, platform=platform)
    if request.method == 'POST':
        form = SocialMediaForm(request.POST, instance=social_media_link)
        if form.is_valid():
            form.save()
            return redirect('social_media')
    form = SocialMediaForm(instance=social_media_link)
    context = {
        'form': form,
        'link': social_media_link,
    }
    return render(request, 'dashboard/edit_social_media.html', context)

def delete_social_media(request, platform):
    social_media_link = get_object_or_404(SocialMediaLink, platform=platform)
    social_media_link.delete()
    return redirect('social_media')