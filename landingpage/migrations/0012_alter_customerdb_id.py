# Generated by Django 5.0.7 on 2024-08-08 05:38

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0011_alter_customerdb_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdb',
            name='id',
            field=models.CharField(default=uuid.UUID('0aef5852-fc33-4bf1-87d1-bf24cf65fd27'), max_length=36),
        ),
    ]