from django.shortcuts import render

# Create your views here.
def purchasebill(request):
    return render(request,"purchasebill.html")
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
    
