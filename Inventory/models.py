from django.db import models

# Create your models here.
class Sales_Party(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    gst_number = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    company_owner = models.CharField(max_length=50)
class Purchase_Party(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    gst_number = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    company_owner = models.CharField(max_length=50)


class FinishGoods(models.Model):
    FG_name=models.CharField(max_length=50)
    FG_qty=models.IntegerField()

class RawMaterial(models.Model):
    RM_name=models.CharField(max_length=50)
    RM_qty=models.IntegerField()
class WastageItem(models.Model):
    WI_name=models.CharField(max_length=50)
    WI_qty=models.IntegerField()
class Production_Report(models.Model):
    genrate_date=models.DateTimeField()
    RM=models.ForeignKey(RawMaterial,on_delete=models.CASCADE)
    WI=models.ForeignKey(WastageItem,on_delete=models.CASCADE)
    FG=models.ForeignKey(FinishGoods,on_delete=models.CASCADE)

class Inventory(models.Model):
    Inventory_name=(('p','production'),
                    ('S','Sales'),
                    ('U','Purchase'))
    S_name=models.CharField(max_length=1,choices=Inventory_name)
    Item_name=models.CharField(max_length=55)
    Item_qty=models.IntegerField()



    








