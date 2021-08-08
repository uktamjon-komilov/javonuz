from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import UserManager


class User(AbstractBaseUser):
    username = models.CharField(max_length=20, unique=True)
    fullname = models.CharField(max_length=100)

    date_joined = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = UserManager()


    def has_perm(self, perm, obj=None):
        return True
    

    def has_module_perms(app_label):
        return True


    def __str__(self):
        return self.username