from django.db import models
from Inventory.models import Purchase_Party 
from Inventory.models import Sales_Party
from Inventory.models import RawMaterial,FinishGoods,Inventory
from datetime import datetime
from django.utils import timezone

# Create your models here.




    
class SalesBill(models.Model):
    party=models.ForeignKey (Sales_Party,on_delete=models.CASCADE)
    date_of_genrate=models.DateField(default=timezone.now)
    Totall_amt=models.DecimalField(max_digits=10, decimal_places=2, default=0)

class sales_item(models.Model):
    inventory=models.ForeignKey(Inventory,on_delete=models.CASCADE)
    sales=models.ForeignKey(SalesBill,on_delete=models.CASCADE)
    FG_name=models.CharField(max_length=50)
    FG_qty=models.IntegerField()
    FG_price=models.IntegerField()
    
class PurchaseBill(models.Model):
    party=models.ForeignKey (Purchase_Party,on_delete=models.CASCADE)
    date_of_genrate=models.DateTimeField()
    Totall_amt=models.DecimalField(max_digits=10, decimal_places=2, default=0)
class purchase_item(models.Model):
    inventory=models.ForeignKey(Inventory,on_delete=models.CASCADE)
    purchase=models.ForeignKey(PurchaseBill,on_delete=models.CASCADE)
    RM_name=models.CharField(max_length=50)
    RM_qty=models.IntegerField()
    RM_price=models.IntegerField()
    
class MisCExp(models.Model):
    sales_Id=models.ForeignKey(FinishGoods,on_delete=models.CASCADE)
    P_party=models.ForeignKey (Purchase_Party,on_delete=models.CASCADE)
    S_party=models.ForeignKey (Sales_Party,on_delete=models.CASCADE)
    date_of_genrate=models.DateTimeField()
    Totall_amt=models.DecimalField(max_digits=10, decimal_places=2, default=0)
class Payment_paid(models.Model):
    date=models.DateField(default=timezone.now)
    purchase_party=models.ForeignKey(Purchase_Party,on_delete=models.CASCADE)
    purchase_party_name=models.CharField(max_length=50)
    paid_date=models.DateField()
    amt_paid=models.DecimalField(max_digits=10, decimal_places=2, default=0)
class Payment_Received(models.Model):
    date=models.DateField(default=timezone.now)
    sales_party=models.ForeignKey(Sales_Party,on_delete=models.CASCADE)
    sales_party_name=models.CharField(max_length=50)
    paid_date=models.DateField()
    amt_paid=models.DecimalField(max_digits=10, decimal_places=2, default=0)
class debtors(models.Model):
    D_name=models.ForeignKey(Sales_Party,on_delete=models.CASCADE)
    sales=models.ForeignKey(SalesBill,on_delete=models.CASCADE)
    remaining_amt=models.DecimalField(max_digits=10,decimal_places=2,default=0)
class creditors(models.Model):
    C_name=models.ForeignKey(Purchase_Party,on_delete=models.CASCADE)
    Purchase=models.ForeignKey(PurchaseBill,on_delete=models.CASCADE)
    remaining_amt=models.DecimalField(max_digits=10,decimal_places=2,default=0)




    
