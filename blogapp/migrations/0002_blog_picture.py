# Generated by Django 3.2.9 on 2021-11-22 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='picture',
            field=models.ImageField(blank=True, upload_to='picture'),
        ),
    ]