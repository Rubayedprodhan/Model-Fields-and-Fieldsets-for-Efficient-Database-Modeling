# Generated by Django 5.1 on 2024-08-14 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentmodel',
            name='file_field',
        ),
        migrations.RemoveField(
            model_name='studentmodel',
            name='file_path_field',
        ),
    ]
