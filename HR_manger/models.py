from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )

    name = models.CharField(max_length=100)
    phone_number = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(10)],
        unique=True
    )
    aadhar_no = models.CharField(
        max_length=12,
        validators=[MinLengthValidator(12)],
        unique=True
    )
    location = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    position = models.CharField(max_length=100)
    date_of_joining = models.DateField()

class Emp_WorkHour(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
class Emp_Salary(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2)
    total_hours_worked = models.FloatField(default=0)
    total_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
