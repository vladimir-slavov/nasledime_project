from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from nasledime_project.profiles.managers import NasledimeUserManager


class NasledimeUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'email'

    objects = NasledimeUserManager()

    class Meta:
        permissions = (
            ('add_will', 'can_add_will'),
            ('change_will', 'can_change_will'),
            ('delete_will', 'can_delete_will'),
            ('view_will', 'can_view_will'),
        )


class Profile(models.Model):
    user = models.OneToOneField(
        NasledimeUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

