# Generated by Django 3.2.9 on 2021-11-26 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_auto_20211123_0737'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='picture',
            new_name='image',
        ),
    ]