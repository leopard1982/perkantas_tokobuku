# Generated by Django 5.0.7 on 2024-08-08 05:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0003_book_kategori_book_pdf_full_book_pdf_prev'),
        ('landingpage', '0012_alter_customerdb_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='view',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.CharField(blank=True, default='', max_length=40, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Book_Review',
            fields=[
                ('id', models.CharField(blank=True, max_length=36, primary_key=True, serialize=False)),
                ('id_buku', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='adminpage.book')),
                ('id_customer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='landingpage.customerdb')),
            ],
            options={
                'unique_together': {('id_buku', 'id_customer')},
            },
        ),
    ]