# Generated by Django 5.1 on 2024-08-13 05:21

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0019_alter_customerbook_id_book_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdb',
            name='id_customer',
            field=models.CharField(blank=True, default='', max_length=50, serialize=False, verbose_name='Data Dari Literatur'),
        ),
        migrations.AlterField(
            model_name='customerdb',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
