# Generated by Django 2.2 on 2019-04-25 02:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20190424_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='D.O.B.'),
        ),
    ]