from django.db import models
from landingpage.models import customerDb

import uuid

tipe = [
	('free','free'),
	('subscribe','subscribe'),
	('buy','buy')
]

kategori = [
	('PA','PA'),
	('Pemuridan','Pemuridan')
]

class Book(models.Model):
	id = models.CharField(max_length=40,default="",primary_key=True,blank=True)
	judul = models.CharField(max_length=100,default="",verbose_name="Nama Buku")
	pengarang = models.CharField(max_length=100,default="",verbose_name="Pengarang Buku")
	price = models.PositiveIntegerField(default=0,verbose_name="Harga Buku")
	isbn = models.CharField(max_length=50,default="",verbose_name="Kode ISBN")
	halaman= models.PositiveIntegerField(default=0,verbose_name="Jumlah Halaman")
	deskripsi = models.TextField(default="",verbose_name="Deskripsi Singkat")
	point = models.PositiveIntegerField(default=0,verbose_name="Point")
	tipe = models.CharField(max_length=20,default="",choices=tipe)
	pdf_full = models.FileField(upload_to="pdf_full",verbose_name="File PDF Full")
	pdf_prev = models.FileField(upload_to="pdf_prev",verbose_name="File PDF Preview")
	kategori = models.CharField(max_length=20,choices=kategori)
	view = models.PositiveBigIntegerField(default=0)

	def save(self,*args,**kwargs):
		self.id=str(uuid.uuid4())
		super(Book,self).save(*args,**kwargs)

	def __str__(self):
		return f"{self.judul}"

class Book_Review(models.Model):
	id = models.CharField(primary_key=True,max_length=36,blank=True)
	id_buku = models.ForeignKey(Book,on_delete=models.RESTRICT)
	id_customer = models.ForeignKey(customerDb,on_delete=models.RESTRICT)
	review = models.TextField(max_length=200)
	updated_review = models.DateField(auto_now_add=True)
	is_published = models.BooleanField(default=False)

	
	def save(self,*args,**kwargs):
		self.id=str(uuid.uuid4())
		super(Book_Review,self).save(*args,**kwargs)

	def __str__(self):
		return f"{self.id_customer.username}"

	class Meta:
		unique_together = ['id_buku','id_customer']