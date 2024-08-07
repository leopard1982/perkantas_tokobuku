from django.db import models
import uuid
import hashlib

colornya = [
	('pink','pink'),
	('blue','blue'),
	('red','red'),
	('yellow','yellow'),
	('green','green'),
	('chocolate','chocolate'),
	('cyan','cyan'),
	('magenta','magenta'),
	('purple','purple'),
	('violet','violet'),
	('grey','grey')
]

payment = [
	('BCA','BCA'),
	('Mandiri','Mandiri')
]

leveling = [
	('silver','silver'),
	('gold','gold'),
	('platinum','platinum')
]

#buku a b c --> silver --> 20rb --> semi google point ditandai
#tanda 1 buku dibaca --> totalan 10.000.000 --> buku sering dibaca --> % keuntungan 
#buku d e f --> gold --> 50rb 
#buku g h i --> platinum --> 100rb
##counting klik buku reset setiap awal bulan
#preview...
#buku lifetime --> buku i

# Create your models here.
class customerDb(models.Model):
	id = models.CharField(max_length=36,default=uuid.uuid4())
	id_customer = models.CharField(max_length=50,verbose_name="Data Dari Literatur")
	user_name = models.SlugField(max_length=256,primary_key=True,null=False,blank=False,verbose_name="User Name")
	alias = models.CharField(max_length=256,null=True,blank=True,verbose_name="Nama Panggilan")
	secret = models.CharField(max_length=256,verbose_name="Password")
	email = models.EmailField(blank=True,null=True)
	birthday = models.DateField(auto_now_add=False,blank=True,null=True)
	photo = models.ImageField(upload_to='profile',null=True,blank=True)
	total_poin = models.PositiveSmallIntegerField(default=0)
	levelling = models.CharField(max_length=20,choices=leveling)

	def __str__(self):
		return f"{self.user}"

	def save(self,*args,**kwargs):
		x = hashlib.new('SHA256')
		x.update(self.secret.encode())
		self.secret = x.hexdigest()
		super(customerDb,self).save(*args,**kwargs)

class customerBook(models.Model):
	id_book = models.CharField(primary_key=True,max_length=36)
	user = models.ForeignKey(customerDb,on_delete=models.RESTRICT)
	kode_buku = models.CharField(max_length=36)
	last_page = models.PositiveSmallIntegerField(default=0)
	booked_date = models.DateField(auto_now_add=False,blank=True,null=True)
	payment = models.CharField(max_length=20,choices=payment)
	payment_code = models.CharField(max_length=100,null=True,blank=True)
	point = models.PositiveSmallIntegerField(default=0)

	def save(self,*args,**kwargs):
		self.id_book = str(uuid.uuid4())
		super(customerBook,self).save(*args,**kwargs)

	def __str__(self):
		return f"{self.id_book}"

class customerBookmark(models.Model):
	id_bookmark = models.CharField(primary_key=True,max_length=36)
	id_book = models.ForeignKey(customerBook,on_delete=models.RESTRICT)
	page = models.PositiveSmallIntegerField(default=1)
	color = models.CharField(max_length=20,choices=colornya)
	note = models.TextField(max_length=2000,null=True,blank=True)
	is_penting = models.BooleanField(default=False)

	def save(self,*args,**kwargs):
		self.id_bookmark = uuid.uuid4()
		super(customerBookmark,self).save(*args,**kwargs)

	def __str__(self):
		return f"{self.id_bookmark}"