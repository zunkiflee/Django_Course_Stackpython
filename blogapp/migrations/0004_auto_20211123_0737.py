# Generated by Django 3.2.9 on 2021-11-23 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_auto_20211123_0735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='featured_pic',
        ),
        migrations.AddField(
            model_name='blog',
            name='picture',
            field=models.ImageField(blank=True, upload_to='picture'),
        ),
    ]
