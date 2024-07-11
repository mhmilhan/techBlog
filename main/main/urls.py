
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from blog import views as search


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path("__reload__/", include("django_browser_reload.urls")),
    path('posts/search/', search.search, name='search'),
    path('', include('accounts.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('', include('blog.urls')),



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
