# Generated by Django 3.2.9 on 2021-11-23 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_blog_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='picture',
        ),
        migrations.AddField(
            model_name='blog',
            name='featured_pic',
            field=models.ImageField(blank=True, upload_to='featured_pic'),
        ),
    ]
