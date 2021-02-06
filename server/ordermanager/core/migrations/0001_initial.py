# Generated by Django 3.1.6 on 2021-02-06 03:24

from django.db import migrations, models
import django.db.models.deletion
import ordermanager.core.models.pegawai


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bagian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_bagian', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_barang', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pegawai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(blank=True, max_length=32, unique=True)),
                ('nama_pegawai', models.CharField(blank=True, max_length=32)),
                ('alamat_pegawai', models.CharField(blank=True, max_length=64)),
                ('hp_pegawai', models.CharField(blank=True, max_length=16)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('id_bagian', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='core.bagian')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', ordermanager.core.models.pegawai.UserManager()),
            ],
        ),
    ]