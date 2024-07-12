from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=25, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name

class Tag(models.Model):
    tag_name = models.CharField(max_length=25, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.tag_name

STATUS_CHOICES = (
    ("draft", "Draft"),
    ("published", "Published")
)


class Post(models.Model):
    title = models.CharField(max_length=125)
    slug = models.SlugField(max_length=175, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=200)
    short_description = models.TextField(max_length=2000)
    content = models.TextField(max_length=5000)
    status = models.CharField(max_length=10, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft')
    is_featured = models.BooleanField(default=False)
    is_latest = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)
    is_unboxing = models.BooleanField(default=False)
    is_review = models.BooleanField(default=False)
    is_ai = models.BooleanField(default=False)
    is_invention = models.BooleanField(default=False)
    is_robotics = models.BooleanField(default=False)
    is_space = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.status == 'published' and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)