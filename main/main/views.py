from django.shortcuts import render
from blog.models import Category


def index(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'base.html', context)

