from django.urls import path
from . import views

urlpatterns = [
    path('purchasebill/', views.purchasebill, name='purchasebill'),
    path('salesbill/', views.salesbill, name='salesbill'),
    path('paymentreceived/', views.paymentreceived, name='paymentreceived'),
    path('paymentpaid/', views.paymentpaid, name='paymentpaid'),
    path('miscelleneousexpanse/', views.Misc, name='Misc'),
    path('creditors/', views.creditors, name='creditors'),
    path('debtors/', views.debtors, name='debtors'),
]