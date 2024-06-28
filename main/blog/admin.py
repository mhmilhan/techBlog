from django.contrib import admin

# Register your models here.
from .models import Category, Tag, Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'status', 'is_featured']
    search_fields = ['id', 'category__category_name', 'title', 'author']
    list_editable = ['status', 'is_featured']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
