from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        unique=True,
        max_length=5,
        blank=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    zip_code = models.CharField(blank=True, max_length=5)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    USERNAME = "email"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
