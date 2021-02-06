from django.db import models

class Bagian(models.Model):
    nama_bagian = models.CharField(max_length=16)