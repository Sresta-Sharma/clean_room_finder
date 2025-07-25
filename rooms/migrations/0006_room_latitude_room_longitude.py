# Generated by Django 5.2.3 on 2025-07-07 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_bookmark'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='latitude',
            field=models.FloatField(default=27.7172),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='longitude',
            field=models.FloatField(default=85.324),
            preserve_default=False,
        ),
    ]
