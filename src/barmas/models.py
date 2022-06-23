from django.db import models
from datetime import datetime, date

# Create your models here.
class Bmasuk(models.Model):
    j_ikan = models.CharField(default="", max_length = 100, blank= False)
    k_ikan = models.IntegerField(blank=False)
    ket = models.CharField(default="", max_length = 10, blank= False)
    m_kend = models.CharField(max_length = 100, blank= False)
    p_kend = models.CharField(default="" , max_length = 100, blank= False)
    harga = models.IntegerField(default=0, blank=False) 
    t_datang = models.DateField(auto_now_add=False, auto_now=False, blank=False)
    b_gambar = models.CharField(max_length = 999999999, blank=False)