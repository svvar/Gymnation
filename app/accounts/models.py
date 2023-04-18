from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class GymUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, phone, email, password):
        if not email:
            raise ValueError("Email field is required")
        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name, phone=phone, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # def create_superuser(self, email, password=None, **extra_fields):
    #     extra_fields.setdefault('is_staff', True)
    #     extra_fields.setdefault('is_superuser', True)
    #
    #     if extra_fields.get('is_staff') is not True:
    #         raise ValueError('Superuser must have is_staff=True.')
    #     if extra_fields.get('is_superuser') is not True:
    #         raise ValueError('Superuser must have is_superuser=True.')
    #
    #     return self.create_user(email, password, **extra_fields)

    def create_staffuser(self, first_name, last_name, phone, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            first_name,
            last_name,
            phone,
            email,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, phone, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            first_name,
            last_name,
            phone,
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class GymUser(AbstractBaseUser, PermissionsMixin):
    CLUB_CHOICES = (
        ("Київ, вул. Уявна 12", "Київ, вул. Уявна 12"),
        ("Київ, вул. Нова 26", "Київ, вул. Нова 26"),
        ("Київ, вул. Довга 102", "Київ, вул. Довга 102"),
        ("Київ, вул. Чудова 19", "Київ, вул. Чудова 19"),
        ("Київ, вул. Зелена 66", "Київ, вул. Зелена 66"),
        ("Київ, вул. Технологічна 8", "Київ, вул. Технологічна 8")
    )

    PLANS_CHOICES = (
        ('STARTER', 'STARTER'),
        ('STANDARD', 'STANDARD'),
        ('PREMIUM', 'PREMIUM'),
        ('PREMIUM SPA', 'PREMIUM SPA')
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    photo = models.ImageField(upload_to='mediaStorage/users', null=True, blank=True)
    club = models.CharField(max_length=100, choices=CLUB_CHOICES, null=True, blank=True)
    plan = models.CharField(max_length=20, choices=PLANS_CHOICES, null=True, blank=True)
    # trainer = models.CharField(max_length=100)

    is_staff = models.BooleanField(default=False, null=True, blank=True)  # a admin user; non super-user
    is_superuser = models.BooleanField(default=False, null=True, blank=True)  # a superuser

    objects = GymUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    def __str__(self):
        return self.email
