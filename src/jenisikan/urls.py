from django.urls import path
from . import views

app_name = 'jenisikan'
urlpatterns = [
    path('', views.halaman_produk, name='halamanproduk'), 
    path('tambahproduk/', views.tambah_jenis_ikan, name='tambahjenisikan'),
    path('editproduk/<int:id>/', views.edit_produk, name='editproduk'),
    path('hapusproduk/<int:id>/', views.hapus_produk, name='hapusproduk'),
]