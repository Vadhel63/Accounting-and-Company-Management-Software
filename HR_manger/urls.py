from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.employee, name='employee'),
    path('employee1/', views.employee1, name='employee1'),
    path('employeedisplay/', views.employeedisplay, name='employeedisplay'),
    path('employeesalary/', views.employeesalary, name='employeesalary'),
    path('employeework/', views.employeework, name='employeework'),
    path('delete_employee/<int:e_id>/', views.delete_employee, name='delete_employee'),
    path('update_employee/<int:e_id>/', views.update_employee, name='update_employee'),
]
