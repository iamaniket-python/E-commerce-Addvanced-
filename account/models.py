from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Custom Manager
class AccountManager(BaseUserManager):
    def create_user(self, firstname, lastname, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            firstname=firstname,
            lastname=lastname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, firstname, lastname, username, email, password=None):
        user = self.create_user(
            email=email,
            username=username,
            firstname=firstname,
            lastname=lastname,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Custom User Model
class Account(AbstractBaseUser):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    phonenumber = models.CharField(max_length=100)

    date_join = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'firstname', 'lastname']

    # Registering custom manager
    objects = AccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
