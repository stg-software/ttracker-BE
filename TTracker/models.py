from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Custom manager for the CustomUser model
class CustomUserManager(BaseUserManager):
    def create_user(self, email, nombre, aPat, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es requerido')
        email = self.normalize_email(email)
        user = self.model(email=email, nombre=nombre, aPat=aPat, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nombre, aPat, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, nombre, aPat, password, **extra_fields)

# Custom user model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=30)  # Reemplaza 'first_name'
    aPat = models.CharField(max_length=30)    # Reemplaza 'last_name'
    aMat = models.CharField(max_length=30, blank=True, null=True)  # Nuevo campo para apellido materno
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'aPat']  # Campos requeridos además del email

    def __str__(self):
        return self.email
