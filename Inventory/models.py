from django.db import models
from datetime import datetime
from django.utils import timezone
from django.core.validators import RegexValidator,MinLengthValidator
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models

class StaffProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)
    name = models.CharField(max_length=255, default='Unknown')
    position = models.CharField(max_length=255, default='HR_Manager')
    email = models.EmailField(max_length=255, default='example@example.com')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='O')
    phone_number = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(10)],
        unique=True
    )

# Create your models here.
class Sales_Party(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(10)],
        unique=True
    )
    gst_regex = RegexValidator(
        regex=r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}[Z]{1}[0-9A-Z]{1}$',
        message="Enter a valid GST number (e.g., 12ABCDE1234F1Z1)."
    )
    gst_number = models.CharField(
        max_length=15,
        validators=[gst_regex],
        unique=True
    )
    location = models.CharField(max_length=255)
    company_owner = models.CharField(max_length=50)
class Purchase_Party(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(10)],
        unique=True
    )
    gst_regex = RegexValidator(
        regex=r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}[Z]{1}[0-9A-Z]{1}$',
        message="Enter a valid GST number (e.g., 12ABCDE1234F1Z1)."
    )
    gst_number = models.CharField(
        max_length=15,
        validators=[gst_regex],
        unique=True
    )
    location = models.CharField(max_length=255)
    company_owner = models.CharField(max_length=50)


class FinishGoods(models.Model):
    FG_name=models.CharField(max_length=50)
class RawMaterial(models.Model):
    RM_name=models.CharField(max_length=50)
class WastageItem(models.Model):
    WI_name=models.CharField(max_length=50)
class Production_Report(models.Model):
    genrate_date=models.DateTimeField()
    RM=models.ForeignKey(RawMaterial,on_delete=models.CASCADE)
    RM_qty=models.IntegerField(default=2)
    WI=models.ForeignKey(WastageItem,on_delete=models.CASCADE)
    WI_qty=models.IntegerField(default=0)
    FG=models.ForeignKey(FinishGoods,on_delete=models.CASCADE)
    FG_qty=models.IntegerField(default=1)

class Inventory(models.Model):
    Item_name=models.CharField(max_length=55)
    Item_qty=models.IntegerField()




    








