# Generated by Django 3.1.6 on 2021-02-17 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='exceprt',
            new_name='excerpt',
        ),
    ]
