from django.shortcuts import render, HttpResponse
from datetime import datetime
import hashlib

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
    context= {
        'tanggal':getTanggal()
    }    
    return render(request,'landing/index.html',context)

def testPDF(request):
    context = {
        'test':'test yow berhasil'
    }
    return render(request,'landing/testpdf.html',context)