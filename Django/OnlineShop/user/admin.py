from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from . models import Teacher, Profile

admin.site.register(Profile)
