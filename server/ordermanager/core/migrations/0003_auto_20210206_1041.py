# Generated by Django 3.1.6 on 2021-02-06 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_pemesanan_pengambilan_produksi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pegawai',
            name='id_bagian',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.bagian'),
        ),
    ]
