# Generated by Django 5.1.2 on 2025-01-10 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pilots', '0018_alter_pilot_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pilot',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='pilots/'),
        ),
    ]