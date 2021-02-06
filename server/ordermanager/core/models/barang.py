from django.db import models

class Barang(models.Model):
    nama_barang = models.CharField(max_length=32, unique=True)