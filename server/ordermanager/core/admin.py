from django.contrib import admin

# Register your models here.
from .models import (
    Bagian,
    Barang,
    Pegawai,
    Pemesanan,
    Pengambilan,
    Produksi
)

class BarangAdmin(admin.ModelAdmin):
    list_display = ('nama_barang',)    


admin.site.register(Bagian)
admin.site.register(Barang, BarangAdmin)
admin.site.register(Pegawai)
admin.site.register(Pemesanan)
admin.site.register(Pengambilan)
admin.site.register(Produksi)