# Generated by Django 3.1.5 on 2021-03-08 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Pessoas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplina',
            name='data_fim',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='data_inicio',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='info',
            field=models.TextField(blank=True, null=True),
        ),
    ]
