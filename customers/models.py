from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager



class User(AbstractUser):
    PH = 'ph'
    PL = 'pl'
    COUNTRY_CHOICES = (
        (PH, 'Philippines'),
        (PL, 'Poland'),
    )

    ADMIN = 1
    SELLER = 2
    CUSTOMER = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (SELLER, 'Seller'),
        (CUSTOMER, 'Customer'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=CUSTOMER)
    street = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=250, blank=True)
    state = models.CharField(max_length=250, blank=True)
    zip_code = models.CharField(max_length=250, blank=True)
    country = models.CharField(
        max_length=250, blank=True, default=PH, choices=COUNTRY_CHOICES)

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
