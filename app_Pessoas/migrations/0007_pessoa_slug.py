# Generated by Django 3.1.5 on 2021-01-29 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Pessoas', '0006_auto_20210126_0743'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
