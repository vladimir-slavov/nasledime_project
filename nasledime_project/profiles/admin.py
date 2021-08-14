from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from nasledime_project.profiles.models import NasledimeUser

admin.site.register(NasledimeUser)