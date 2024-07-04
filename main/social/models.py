from django.db import models

# Create your models here.
class SocialMediaLink(models.Model):
    PLATFORM_CHOICES = [
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('instagram', 'Instagram'),
        ('youtube', 'YouTube'),
        ('whatsapp', 'WhatsApp'),
        ('telegram', 'Telegram'),
        ('discord', 'Discord'),
        ('reddit', 'Reddit'),
    ]

    platform = models.CharField(max_length=25, choices=PLATFORM_CHOICES)
    url = models.URLField(max_length=250)
    icon_class = models.CharField(max_length=100)

    def __str__(self):
        return self.platform