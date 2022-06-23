from django.urls import path
from . import views

app_name = 'barmas'
urlpatterns = [
    path('', views.tabel, name='tabel'),
    path('tambah/', views.awal, name='awal'),
    path('edit/<int:id>/', views.edit_awal, name='edit'), 
    path('delete/<int:id>/', views.delete_awal, name='delete'),  
]