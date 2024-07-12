from django import forms
from blog.models import Post, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title', 'category', 'tags', 'featured_image', 'caption',
            'short_description', 'content', 'status', 'is_featured',
            'is_latest', 'is_popular', 'is_trending', 'is_unboxing',
            'is_review', 'is_ai', 'is_invention', 'is_robotics', 'is_space'
        ]