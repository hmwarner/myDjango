# Generated by Django 2.2 on 2019-04-25 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_about_me'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='about_me',
        ),
    ]
