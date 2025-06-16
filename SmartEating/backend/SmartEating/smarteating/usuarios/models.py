from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email,first_name,last_name, password,**extra_fields):
            """
            Creates and saves a User with the given email and password.
            """
            if not email:
                raise ValueError("Ha de proporcionar un e-mail válido")

            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)

            user.set_password(password)
            
            user.set_password(password)
            user.is_staff = True
            user.is_active = True
            user.is_superuser = True
            user.save()
            return user    

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    url = models.URLField(max_length=255, default='https://i.imgur.com/Yt69VC0.jpg')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    def get_full_name(self):
        return self.first_name + self.last_name

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser   
    
    def __str__(self):
        return self.email