from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def employee(request):
    return render(request,"employee.html")
def employeework(request):
    return render(request,"employeework.html")
def employeesalary(request):
    return render(request,"employeesalary.html")
