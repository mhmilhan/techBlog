# Generated by Django 5.0.6 on 2024-07-04 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(choices=[('facebook', 'Facebook'), ('twitter', 'Twitter'), ('instagram', 'Instagram'), ('youtube', 'YouTube'), ('whatsapp', 'WhatsApp'), ('telegram', 'Telegram'), ('discord', 'Discord'), ('reddit', 'Reddit')], max_length=25)),
                ('url', models.URLField(max_length=250)),
                ('icon_class', models.CharField(max_length=100)),
            ],
        ),
    ]
