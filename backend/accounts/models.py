from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models

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


from django.core.validators import MinValueValidator, MaxValueValidator

class UserBodyInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name="user_body_info")

    age = models.IntegerField(validators=[MinValueValidator(20), MaxValueValidator(120)])
    height = models.IntegerField(validators=[MinValueValidator(145), MaxValueValidator(230)])
    weight = models.IntegerField(validators=[MinValueValidator(50), MaxValueValidator(150)])
    gender = models.CharField(max_length=2)
    general = models.FloatField(validators=[MinValueValidator(1.2), MaxValueValidator(1.6)])
    excise = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(0.3)])

    created_at = models.DateTimeField(auto_now_add=True)


class BodyInfoRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="body_info_record")
    
    week_diet = models.ForeignKey("diets.WeekDiet", on_delete=models.CASCADE, null=True, related_name="body_info_record")
    age = models.IntegerField(validators=[MinValueValidator(20), MaxValueValidator(120)])
    height = models.IntegerField(validators=[MinValueValidator(145), MaxValueValidator(230)])
    weight = models.IntegerField(validators=[MinValueValidator(50), MaxValueValidator(150)])
    gender = models.CharField(max_length=2)
    general = models.FloatField(validators=[MinValueValidator(1.2), MaxValueValidator(1.6)])
    excise = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(0.3)])

    created_at = models.DateTimeField(auto_now_add=True)