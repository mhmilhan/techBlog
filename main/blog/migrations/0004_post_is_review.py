# Generated by Django 5.0.6 on 2024-06-29 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_is_latest_post_is_popular_post_is_trending_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_review',
            field=models.BooleanField(default=False),
        ),
    ]