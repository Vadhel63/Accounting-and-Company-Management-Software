from django.contrib import admin
from. models import *


# Register your models here.

admin.site.register(SalesBill)
admin.site.register(PurchaseBill)
admin.site.register(sales_item)
admin.site.register(purchase_item)
admin.site.register(Payment_paid)
admin.site.register(Payment_Received)
admin.site.register(MisCExp)
admin.site.register(MisCExp_item)
admin.site.register(debtors)
admin.site.register(creditors)

