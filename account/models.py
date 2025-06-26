from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class CustomUserManager(AbstractBaseUser):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    username=models.CharField(max_length=100,unique=True)
    email=models.EmailField(unique=True)
    phonenumber=models.CharField(max_length=100)

    date_join =models.DateTimeField(auto_now_add=True)
    last_login =models.DateTimeField(auto_now=True)

    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','firstname','lastname']

    def __str__(self):
        return self.email
    
    def permissions(self,permissions, obj=None):
        return self.is_admin
    
    def module_persmissions(self, obj=None):
        return True
    
class Manager(CustomUserManager):
    def create_superuser(self,firstname,lastname,username,email,password=None):
        if not email:
            raise ValueError('User must have an email address'
            )
        if not username:
            raise ValueError('User must have an username')
        user=self.model(
            email=self.normalize_email(email),
            username=username,
            firstname=firstname,
            lastname=lastname,
        )
       