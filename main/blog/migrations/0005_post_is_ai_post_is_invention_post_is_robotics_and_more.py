# Generated by Django 5.0.6 on 2024-06-29 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_is_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_ai',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='is_invention',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='is_robotics',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='is_space',
            field=models.BooleanField(default=False),
        ),
    ]
