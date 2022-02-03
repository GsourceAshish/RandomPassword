from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import CustomUserManager
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractBaseUser,PermissionsMixin):
    username = None
    
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    first_name = models.CharField(blank=True, max_length=100)
    last_name = models.CharField(blank=True, max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    # is_superuser = models.BooleanField(default=False)\

    def get_email(self):
        return self.first_name + ' belongs to ' + self.email + ' email.'    
    
    def __str__(self):
        return self.email
