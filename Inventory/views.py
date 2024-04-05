from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from Inventory.models import *
# Create your views here.
import json

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
    # Assuming you have FinishGoods and RawMaterial models
    fg = FinishGoods.objects.all()
    raw = RawMaterial.objects.all()

    return render(request, 'p_Report.html', {'fg': fg, 'raw': raw})

def DisplayPR(request):
    date=request.POST['date']
    fg_n=request.POST['clickcount1']
    rm_n=request.POST['clickcount2']
    print("-------------------------------------\n")
    print("fg n = ",fg_n)
    print("rm n = ",rm_n)
    print("-------------------------------------\n")
    prod_repo = Production_Report.objects.create(genrate_date=date)
    for i in range(0,int(rm_n)+1):
        r = request.POST.get('r_name' + str(i))
        print("-------------------------------------\n")
        print(r)
        rm = RawMaterial.objects.get(RM_name=r)
        print(rm)
        print("-------------------------------------\n")
        inven = Inventory.objects.get(Item_name=r)
        piece2= int(request.POST.get('rpiece' + str(i)))
        if inven.Item_qty - piece2<0:
            prod_repo.delete()
            return HttpResponse("Insuffieceint Qauntity in Inventory To Accept Production Report")
        inven.Item_qty -=piece2
        inven.save()
        Production_RM.objects.create(production_repo=prod_repo,RM_name=rm,RM_qty=piece2)
    
    for i in range(0,int(fg_n)+1):
        f = request.POST.get('fg' + str(i))
        fg = FinishGoods.objects.get(FG_name=f)
        print("-------------------------------------\n")
        print(f)
        # rm = RawMaterial.objects.get(RM_name=r)
        print(fg)
        print("-------------------------------------\n")
        piece1 = int(request.POST.get('fpiece' + str(i)))
        inven = Inventory.objects.get(Item_name=f)
        inven.Item_qty +=piece1
        inven.save()
        Production_FG.objects.create(production_repo=prod_repo,FG_name=fg,FG_qty=piece1)
    return HttpResponse("SUCCESS")
    # p1=Production_Report(genrate_date=date,RM_qty=piece2,FG_qty=piece1,RM=r,FG=f)
    # p1.save()
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
from django.shortcuts import render, redirect
from .models import RawMaterial

def rawmaterial(request):
    return render(request, "rawmaterial.html")

def displayraw(request):
    if request.method == 'POST':
        raw_name = request.POST['raw']
        raw = RawMaterial.objects.create(RM_name=raw_name)
        Inventory.objects.create(Item_name=raw_name,Item_qty=0)
        raw.save()
        return redirect("displayraw1")
    else:
        return redirect("rawmaterial")  # Redirect if accessed via GET

def displayraw1(request):
    raw = RawMaterial.objects.all()
    return render(request, "displayRM.html", {
        "raw": raw
    })

def delete_raw(request, raw_id):
    if request.method == 'POST':
        raw = RawMaterial.objects.get(id=raw_id)
        raw.delete()
    return redirect("displayraw1")

def update_raw(request, raw_id):
    raw = RawMaterial.objects.get(id=raw_id)
    if request.method == 'POST':
        raw_name = request.POST['raw']
        raw.RM_name = raw_name
        raw.save()
        return redirect("displayraw1")
    else:
        return render(request, "updateRM.html", {
            "raw": raw
        })
#-----------------------------------
    
def wastageitem(request):
    return render(request,"W_Item.html")
#finsih goods----------------------------
def finishgood(request):
    return render(request,"finishgood.html")

def displayfinishgoods(request):
    if request.method == 'POST':
        finishgoodname=request.POST['fg']
        f1=FinishGoods.objects.create(FG_name=finishgoodname)
        Inventory.objects.create(Item_name=finishgoodname,Item_qty=0)
        f1.save()
        return redirect("displayfinishgoods1")
    else:
        return redirect("finishgood") 


    

def displayfinishgoods1(request):
    fg=FinishGoods.objects.all()
    return render(request,"displayFG.html",{
        'fg':fg
    })
    
def delete_fg(request,fg_id):
    if request.method == 'POST':
        fg = FinishGoods.objects.get(id=fg_id)
        fg.delete()
    return redirect("displayfinishgoods1")

def update_fg(request,fg_id):
    fg= FinishGoods.objects.get(id=fg_id)
    if request.method == 'POST':
        name = request.POST['fg']
        fg.FG_name =name
        fg.save()
        return redirect("displayfinishgoods1")
    else:
        return render(request, "updateFG.html", {
            "fg": fg
        })
    print(fg)
#------------------------
