# Generated by Django 5.1.2 on 2024-12-06 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pilots', '0007_pilotinventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='pilot',
            name='market_value',
            field=models.FloatField(blank=True, null=True),
        ),
    ]