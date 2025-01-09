# Generated by Django 5.1.2 on 2025-01-08 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pilots', '0016_autodromo_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autodromo',
            name='data_de_criacao_autodromo',
        ),
        migrations.RemoveField(
            model_name='team',
            name='data_de_criacao',
        ),
        migrations.AddField(
            model_name='autodromo',
            name='ano_de_criacao_autodromo',
            field=models.IntegerField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='ano_de_criacao_team',
            field=models.IntegerField(blank=True, max_length=4, null=True),
        ),
    ]
