# Generated by Django 2.2 on 2019-04-25 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20190424_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about_me',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
