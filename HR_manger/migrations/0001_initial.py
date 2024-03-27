# Generated by Django 4.2.10 on 2024-03-27 08:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('aadhar_no', models.CharField(max_length=12, unique=True, validators=[django.core.validators.MinLengthValidator(12)])),
                ('location', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('position', models.CharField(max_length=100)),
                ('date_of_joining', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Emp_WorkHour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HR_manger.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Emp_Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hourly_rate', models.DecimalField(decimal_places=2, max_digits=8)),
                ('total_hours_worked', models.FloatField(default=0)),
                ('total_salary', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HR_manger.employee')),
            ],
        ),
    ]
