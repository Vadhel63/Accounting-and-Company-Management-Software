from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.employee, name='employee'),
    path('employeesalary/', views.employeesalary, name='employeesalary'),
    path('employeework', views.employeework, name='employeework'),
]