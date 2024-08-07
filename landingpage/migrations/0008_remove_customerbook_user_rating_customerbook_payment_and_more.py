# Generated by Django 5.0.7 on 2024-08-04 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0007_customerbookmark_is_penting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerbook',
            name='user_rating',
        ),
        migrations.AddField(
            model_name='customerbook',
            name='payment',
            field=models.CharField(choices=[('BCA', 'BCA'), ('Mandiri', 'Mandiri')], default='BCA', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customerbook',
            name='payment_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
