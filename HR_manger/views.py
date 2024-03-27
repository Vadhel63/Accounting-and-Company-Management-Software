from django.shortcuts import render,redirect
from django.http import HttpResponse
from HR_manger.models import *
# Create your views here.
def employee(request):
    return render(request,"employee.html")
def employee1(request):
    date=request.POST['date']
    e_name=request.POST['name']
    c_no=request.POST['number']
    adhar_no=request.POST['aadhar']
    location=request.POST['location']
    j_position=request.POST['position']
    gender=request.POST['gender']
    e=Employee.objects.create(name=e_name,phone_number=c_no,aadhar_no=adhar_no,location=location,gender=gender,date_of_joining=date,position=j_position)
    e.save()
    return redirect('employeedisplay')

def employeedisplay(request):
    e=Employee.objects.all()
    return render(request,'employeedisplay.html',{
        'e1':e
    })
def employeework(request):
    return render(request,"employeework.html")
def employeesalary(request):
    return render(request,"employeesalary.html")
