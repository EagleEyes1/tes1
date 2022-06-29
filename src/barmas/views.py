import base64
from django.shortcuts import get_object_or_404, render, redirect
from .models import Bmasuk
from jenisikan.models import JenisIkan
from datetime import datetime

# Create your views here.

def awal(request):
    if request.user.is_authenticated:
        baris = JenisIkan.objects.all()
        if request.method == 'POST':
            jenis_ikan = request.POST.get('jenis_ikan')
            kuantitas = request.POST.get('kuantitas')
            jenis_mobil = request.POST.get('jenis_mobil')
            plat_mobil = request.POST.get('plat_mobil')
            keterangan = request.POST.get('ket')
            expire_date = request.POST.get('expire_date')
            t_datang = datetime.strptime(expire_date, '%m/%d/%Y').strftime('%Y-%m-%d')
            b_gambar = base64.b64encode(request.FILES.get('image').read()).decode()
            
            for object in baris:
                if object.j_ikan == jenis_ikan:
                    if keterangan == "Kg":
                        harga = int(kuantitas) * int(object.h_kg)
                        break
                    else:
                        harga = int(kuantitas) * int(object.h_ton)
                        break
        
            Bmasuk1 = Bmasuk(j_ikan=jenis_ikan, k_ikan=kuantitas, ket=keterangan, m_kend=jenis_mobil, p_kend=plat_mobil, 
            t_datang = t_datang, b_gambar = b_gambar, harga = harga)
            Bmasuk1.save()
            return redirect('../')

        return render(request, 'masuk.html', {'baris': baris, 'pengguna':request.user.username})
    else:
        return redirect('/login/')

def tabel(request):
    if request.user.is_authenticated:
        baris = Bmasuk.objects.all()
        return render(request, 'tabel_masuk.html', {'baris': baris, 'pengguna':request.user.username})
    else: 
        return redirect('/login/')

def edit_awal(request, id):
    if request.user.is_authenticated:
        baris = Bmasuk.objects.get(id=id)
        baris.t_datang = str(datetime.strptime(str(baris.t_datang), '%Y-%m-%d').strftime('%m/%d/%Y'))
        jenisikan1 = JenisIkan.objects.all()
        
        if request.method == 'POST':
            jenis_ikan = request.POST.get('jenis_ikan')
            kuantitas = request.POST.get('kuantitas')
            jenis_mobil = request.POST.get('jenis_mobil')
            plat_mobil = request.POST.get('plat_mobil')
            keterangan = request.POST.get('ket')
            expire_date = request.POST.get('expire_date')
            t_datang = datetime.strptime(expire_date, '%m/%d/%Y').strftime('%Y-%m-%d')
            b_gambar = base64.b64encode(request.FILES.get('image').read()).decode()
            
            for object in jenisikan1:
                if object.j_ikan == jenis_ikan:
                    if keterangan == "Kg":
                        harga = int(kuantitas) * int(object.h_kg)
                        break
                    else:
                        harga = int(kuantitas) * int(object.h_ton)
                        break
        
            Bmasuk.objects.filter(id=id).update(j_ikan=jenis_ikan, k_ikan=kuantitas, ket=keterangan, m_kend=jenis_mobil, p_kend=plat_mobil, 
            t_datang = t_datang, b_gambar = b_gambar, harga = harga)
            return redirect('barmas:tabel')
        return render(request, 'edit_masuk.html', {'baris': baris, 'jenisikan':jenisikan1, 'pengguna':request.user.username})
    else: 
        return redirect('/login/')

def delete_awal(request, id):
    if request.user.is_authenticated:
        baris = get_object_or_404(Bmasuk, id=id)
        baris.delete()
        return redirect('barmas:tabel')
    else: 
        return redirect('/login/')

