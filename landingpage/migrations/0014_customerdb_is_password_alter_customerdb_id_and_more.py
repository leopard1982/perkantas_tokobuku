# Generated by Django 5.0.7 on 2024-08-09 03:27

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0013_alter_customerdb_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerdb',
            name='is_password',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customerdb',
            name='id',
            field=models.CharField(default=uuid.UUID('6df922b8-5cbc-4650-a9be-3cb65ace42de'), max_length=36),
        ),
        migrations.AlterField(
            model_name='customerdb',
            name='id_customer',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Data Dari Literatur'),
        ),
    ]
