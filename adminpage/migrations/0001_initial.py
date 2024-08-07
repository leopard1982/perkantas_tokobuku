# Generated by Django 5.0.7 on 2024-08-06 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.CharField(default='', max_length=40, primary_key=True, serialize=False)),
                ('judul', models.CharField(default='', max_length=100, verbose_name='Nama Buku')),
                ('pengarang', models.CharField(default='', max_length=100, verbose_name='Pengarang Buku')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Harga Buku')),
                ('isbn', models.CharField(default='', max_length=50, verbose_name='Kode ISBN')),
                ('halaman', models.PositiveIntegerField(default=0, verbose_name='Jumlah Halaman')),
                ('deskripsi', models.TextField(default='', verbose_name='Deskripsi Singkat')),
            ],
        ),
    ]
