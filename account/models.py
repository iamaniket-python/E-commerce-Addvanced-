from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class CustomUserManager(AbstractBaseUser):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    username=models.CharField(max_length=100,unique=True)
    email=models.EmailField(unique=True)
    phonenumber=models.CharField(max_length=100)

