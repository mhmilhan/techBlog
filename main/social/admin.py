from django.contrib import admin
from .models import SocialMediaLink

# Register your models here.

class SocialMediaLinkAdmin(admin.ModelAdmin):
    list_display = ['platform', 'url']

admin.site.register(SocialMediaLink)