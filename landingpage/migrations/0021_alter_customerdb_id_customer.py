# Generated by Django 5.1 on 2024-08-13 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0020_alter_customerdb_id_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdb',
            name='id_customer',
            field=models.CharField(blank=True, default='', max_length=50, primary_key=True, serialize=False, verbose_name='Data Dari Literatur'),
        ),
    ]
