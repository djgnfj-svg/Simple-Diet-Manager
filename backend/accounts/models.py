from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)


# Create your models here.    


class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        superuser = self.create_user(
            email=email,
            password=password,
        )
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        superuser.save(using=self._db)
        return superuser


class User(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(max_length=30, unique=True, null=False, blank=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class UserBodyInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_body_info")
    height = models.IntegerField()
    weight = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    activity = models.CharField(max_length=50)
    general = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class BodyInfoRecord(models.Model):
    user_body_info = models.ForeignKey(UserBodyInfo, on_delete=models.CASCADE, related_name="records")
    height = models.IntegerField()
    weight = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    activity = models.CharField(max_length=50)
    general = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)