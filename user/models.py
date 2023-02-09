from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
# from phonenumber_field.modelfields import PhoneNumberField

from .signals import create_cart_for_new_user


class NewUser(AbstractUser):
    city = models.CharField(max_length=50, blank=True, null=True)
    mobile_phone = models.IntegerField(blank=True, null=True)
    created = models.BooleanField(
        verbose_name='created',
        default=False,
    )

    # Паказваюцца пры ўвядзеньні токена
    REQUIRED_FIELDS = ['first_name', 'last_name', 'mobile_phone']


post_save.connect(create_cart_for_new_user, sender=NewUser)

