# Generated by Django 5.0.6 on 2024-07-02 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_is_ai_post_is_invention_post_is_robotics_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
