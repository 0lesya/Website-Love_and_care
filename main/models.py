from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    #message = models.TextField(null=True)
    pass


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    nickname = models.CharField(null=True, blank=True, max_length=100)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")

    def __str__(self):
        return str(self.user)


class Comment(models.Model):
    name = models.CharField('name', max_length=100, default="default name")
    email = models.EmailField('email', null=True, default="default email")
    content = models.TextField('content')

    def __str__(self):
        return self.name
