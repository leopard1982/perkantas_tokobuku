from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from datetime import datetime
import hashlib
from adminpage.models import Book_Review, Book
from landingpage.models import customerDb
from pdf2image import convert_from_path
from django.conf import settings
import os
import uuid
import shutil

    
def check_review(id_buku,id_customer):
    try:
        book = Book.objects.get(id=id_buku)
    except:
        return False
    try: 
        customerdb = customerDb.objects.get(id=id_customer)
    except:
        return False
    try:
        book_review = Book_Review.objects.get(id_buku=book,id_customer=customerdb)
        return True
    except:
        return False

def get_waktu():
    mytime = int(datetime.now().hour)
    if mytime<12: return "Pagi"
    elif mytime==12: return "Siang"
    elif mytime<18: return "Sore"
    else: return "Malam"

def hashPassword(passwd):
    h = hashlib.new('SHA256')
    h.update(b"{passwd}")
    return h.hexdigest()

# Create your views here.
def getTanggal():
    tanggal=datetime.now().date().day
    bulan = datetime.now().date().month
    tahun = datetime.now().date().year
    hari = datetime.now().date().weekday()

    if bulan==1: bulan="Januari"
    elif bulan==2: bulan="Februari"
    elif bulan==3: bulan="Maret"
    elif bulan==4: bulan="April"
    elif bulan==5: bulan="Mei"
    elif bulan==6: bulan="Juni"
    elif bulan==7: bulan="Juli"
    elif bulan==8: bulan="Agustus"
    elif bulan==9: bulan="September"
    elif bulan==10: bulan="Oktober"
    elif bulan==11: bulan="November"
    elif bulan==12: bulan="Desember"

    if hari==0: hari="Senin"
    elif hari==1: hari="Selasa"
    elif hari==2: hari="Rabu"
    elif hari==3: hari="Kamis"
    elif hari==4: hari="Jumat"
    elif hari==5: hari="Sabtu"
    elif hari==6: hari="Minggu"

    return f"{hari}, {tanggal} {bulan} {tahun}"

def welcome(request):
    print(request.user.groups)
    context= {
        'waktu':get_waktu(),
        'tanggal':getTanggal()
    }    
    return render(request,'landing/index.html',context)

def testPDF(request):
    files = os.path.join(settings.BASE_DIR,'media','temp')
        # print(f"data {files}")
    shutil.rmtree(files)
    os.mkdir(os.path.join(settings.BASE_DIR,'media','temp'))
    
    halaman=0
    if 'next' in request.GET:
        halaman=int(request.GET['next'])
    elif 'before' in request:
        halaman = int(request.GET['before'])

    if(halaman<0): halaman=0
    
    filename = os.path.join('media','temp',str(uuid.uuid4()) + '.jpg')
    # filename=os.path.join(settings.BASE_DIR,'media',str(uuid.uuid4())+'.jpg')
    print(os.path.join(settings.BASE_DIR,'test.pdf'))
    file_pdf = convert_from_path(os.path.join(settings.BASE_DIR,'test.pdf'),80)
    try:
        file_pdf[halaman].save(os.path.join(settings.BASE_DIR,filename),'JPEG')
    except:
        halaman=0
        file_pdf[0].save(os.path.join(settings.BASE_DIR,filename),'JPEG')
    # if request.user.is_authenticated:
    context = {
            'waktu':get_waktu(),
            'tanggal':getTanggal(),
            'header':'Test PDF Reader',
            'pict':filename,
            'next': halaman+1,
            'before': halaman-1,
            'current': halaman+1
        }

    return render(request,'landing/testpdf.html',context)
    # else:
    #     return HttpResponseRedirect(reverse('test2',kwargs={'test2':'yuhuuuuuu'}))
    
def test2(request,test):
    return HttpResponse('hallo...')