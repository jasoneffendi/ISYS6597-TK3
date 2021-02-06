from django.db import models
from .barang import Barang
from .pemesanan import Pemesanan

class Produksi(models.Model):
    pesanan = models.ForeignKey(Pemesanan, on_delete=models.PROTECT)
    barang = models.ForeignKey(Barang, on_delete=models.PROTECT)
    jumlah_produksi = models.CharField(max_length=16)
    lead_time = models.CharField(max_length=4)