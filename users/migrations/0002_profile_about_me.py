# Generated by Django 2.2 on 2019-04-25 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about_me',
            field=models.TextField(max_length=250, null=True),
        ),
    ]
