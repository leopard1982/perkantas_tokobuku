from django.db import models
import uuid

tipe = [
	('free','free'),
	('subscribe','subscribe'),
	('buy','buy')
]

class Book(models.Model):
	id = models.CharField(max_length=40,default="",primary_key=True)
	judul = models.CharField(max_length=100,default="",verbose_name="Nama Buku")
	pengarang = models.CharField(max_length=100,default="",verbose_name="Pengarang Buku")
	price = models.PositiveIntegerField(default=0,verbose_name="Harga Buku")
	isbn = models.CharField(max_length=50,default="",verbose_name="Kode ISBN")
	halaman= models.PositiveIntegerField(default=0,verbose_name="Jumlah Halaman")
	deskripsi = models.TextField(default="",verbose_name="Deskripsi Singkat")
	point = models.PositiveIntegerField(default=0,verbose_name="Point")
	tipe = models.CharField(max_length=20,default="",choices=tipe)

	def save(self,*args,**kwargs):
		self.id=str(uuid.uuid4())
		super(Book,self).save(*args,**kwargs)
