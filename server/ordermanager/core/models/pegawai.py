from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager

from .bagian import Bagian


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        user = self.model(**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(password, **extra_fields)

    def create_superuser(self, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(password, **extra_fields)


class Pegawai(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=32, blank=True, unique=True)
    nama_pegawai = models.CharField(max_length=32, blank=True)
    alamat_pegawai = models.CharField(max_length=64, blank=True)
    hp_pegawai = models.CharField(max_length=16, blank=True)
    bagian = models.ForeignKey(Bagian, on_delete=models.PROTECT, null=True)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s - %s' % (self.username, self.nama_pegawai)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.username
