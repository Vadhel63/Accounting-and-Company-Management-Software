from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from Inventory.models import *
# Create your views here.
def purchasebill(request):
    purchase=Purchase_Party.objects.all()
    raw=RawMaterial.objects.all()
    return render(request,"purchasebill.html",{
        'purchase':purchase,
        'raw':raw
    })
    
    

    
    
def salesbill(request):
    return render(request,"salesbill.html")
def paymentreceived(request):
    return render(request,"paymentreceived.html")
def paymentpaid(request):
    return render(request,"paymentpaid.html")
def creditors(request):
    return render(request,"creditors.html")
def debtors(request):
    return render(request,"debtors.html")
def Misc(request):
     return render(request,"miscelleneousexpanse.html")
    
