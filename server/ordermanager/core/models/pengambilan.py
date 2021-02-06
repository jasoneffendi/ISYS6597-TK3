from django.db import models
from .barang import Barang

class Pengambilan(models.Model):
    nama_pengambil = models.CharField(max_length=32)
    barang = models.ForeignKey(Barang, on_delete=models.PROTECT)
    jumlah_pengambilan = models.CharField(max_length=16)