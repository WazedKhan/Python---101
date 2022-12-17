from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_image", blank=True, null=True)

    def __str__(self):
        return f'{self.user} - Profile'

