from django.shortcuts import get_object_or_404, render, redirect
from .models import JenisIkan
import base64

# Create your views here.

def tambah_jenis_ikan(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            jenis_ikan = request.POST.get('jenis_ikan')
            harga_per_kilo = request.POST.get('hargakilo')
            harga_per_ton = request.POST.get('hargaton')
            gambar_ikan = base64.b64encode(request.FILES.get('image').read()).decode()
            
            JenisIkan1 = JenisIkan(j_ikan=jenis_ikan, g_ikan=gambar_ikan, h_kg=harga_per_kilo, h_ton=harga_per_ton)
            JenisIkan1.save()
            return redirect('jenisikan:halamanproduk')
        return render(request, 'jenis_ikan.html', {'pengguna':request.user.username})
    else:
        return redirect('/login/')
    

def halaman_produk(request):
    if request.user.is_authenticated:
        baris = JenisIkan.objects.all()
        return render(request, 'tabel_produk.html', {'baris':baris, 'pengguna':request.user.username})
    else:
        return redirect('/login/')

def edit_produk(request, id):
    if request.user.is_authenticated:
        baris = JenisIkan.objects.get(id=id)
        if request.method == 'POST':
            jenis_ikan = request.POST.get('jenis_ikan')
            harga_per_kilo = request.POST.get('hargakilo')
            harga_per_ton = request.POST.get('hargaton')
            gambar_ikan = base64.b64encode(request.FILES.get('image').read()).decode()
            
            JenisIkan.objects.filter(id=id).update(j_ikan=jenis_ikan, g_ikan=gambar_ikan, h_kg=harga_per_kilo, h_ton=harga_per_ton)
            return redirect('jenisikan:halamanproduk')

        return render(request, 'edit_produk.html', {'baris':baris, 'pengguna':request.user.username})
    else:
        return redirect('/login/')

def hapus_produk(request, id):
    if request.user.is_authenticated:
        baris = get_object_or_404(JenisIkan, id=id)
        baris.delete()
        return redirect('jenisikan:halamanproduk')
    else:
        return redirect('/login/')
