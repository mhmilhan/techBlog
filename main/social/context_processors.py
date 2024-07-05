from .models import SocialMediaLink

def get_social_media_links(request):
    social_media_links = SocialMediaLink.objects.all()
    return dict(social_media_links=social_media_links)