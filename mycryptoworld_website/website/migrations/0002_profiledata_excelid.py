# Generated by Django 4.0.6 on 2022-12-10 21:26

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiledata',
            name='excelid',
            field=models.IntegerField(default=6, null=True, verbose_name=django.contrib.auth.models.User),
        ),
    ]
