from django.db import models
from .barang import Barang

class Pemesanan(models.Model):
    nama_pemesan = models.CharField(max_length=32)
    barang = models.ForeignKey(Barang, on_delete=models.PROTECT)
    jumlah_pesanan = models.CharField(max_length=16)
    proses = models.BooleanField(default=False)