from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from Inventory.models import *
# Create your views here.

#sales_party-----------------------------
def sales(request):
    return render(request,"sales.html")
def DisplaySales(request):
    c_name=request.POST['c_name']
    c_no=request.POST['c_no']
    location=request.POST['location']
    gst_no=request.POST['gst_no']
    c_owner=request.POST['c_owner']
    sales1=Sales_Party.objects.create(name=c_name,phone_number=c_no,location=location,gst_number=gst_no,company_owner=c_owner)
    sales1.save()
    return redirect("displaysales1")

def displaysales1(request):
    sales=Sales_Party.objects.all()
    print(sales)
    return render(request,"displaysales1.html",{
        "sales":sales
    })
#---------------------------------
def productionreport(request):
    return render(request, "P_Report.html")


    
#purchase_party------------------------
def displaypurchase1(request):
    purchase=Purchase_Party.objects.all()
    return render(request,"displaypurchase1.html",{
        "purchase":purchase
    })


def DisplayPurchase(request):
    c_name=request.POST['c_name']
    c_no=request.POST['c_no']
    location=request.POST['location']
    gst_no=request.POST['gst_no']
    c_owner=request.POST['c_owner']
    purchase1=Purchase_Party.objects.create(name=c_name,phone_number=c_no,location=location,gst_number=gst_no,company_owner=c_owner)
    purchase1.save()
    return redirect("displaypurchase1")

def purchase(request):
    return render(request,"purchase.html")

#rawmaterial-------------------------------
def rawmaterial(request):
    return render(request,"rawmaterial.html")

def displayraw(request):
    raw_name=request.POST['raw']
   
    raw=RawMaterial.objects.create(RM_name=raw_name)
    raw.save()
    return redirect("displayraw1")

def displayraw1(request):
    raw=RawMaterial.objects.all()
    return render(request,"displayRM.html",{
        "raw":raw
    })
#-----------------------------------
    
def wastageitem(request):
    return render(request,"W_Item.html")
#finsih goods----------------------------
def finishgood(request):
    return render(request,"finishgood.html")

def displayfinishgoods(request):
    finishgoodname=request.POST['fg']
    f1=FinishGoods.objects.create(FG_name=finishgoodname)
    f1.save()
    return redirect("displayfinishgoods1")

def displayfinishgoods1(request):
    f=FinishGoods.objects.all()
    return render(request,"displayfinishgoods.html",{
        'f':f
    })
