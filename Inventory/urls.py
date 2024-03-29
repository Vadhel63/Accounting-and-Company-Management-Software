from django.urls import path
from . import views

urlpatterns = [
   
    path('sales', views.sales, name='sales'),
    path('P_Report', views.productionreport, name='P_Report'),
    path('purchase', views.purchase, name='purchase'),
    
    path('DisplayPurchase', views.DisplayPurchase, name='DisplayPurchase'),
    path('displaypurchase1', views.displaypurchase1, name='displaypurchase1'),
    
    path('DisplaySales', views.DisplaySales, name='DisplaySales'),
    path('displaysales1', views.displaysales1, name='displaysales1'),
    
    path('rawmaterial/', views.rawmaterial, name='rawmaterial'),
    path('displayraw/', views.displayraw, name='displayraw'),
    path('displayraw1/', views.displayraw1, name='displayraw1'),
    path('delete/<int:raw_id>/', views.delete_raw, name='delete_raw'),
    path('update/<int:raw_id>/', views.update_raw, name='update_raw'),
    
    path('W_Item', views.wastageitem, name='W_Item'),
    
    path('finishgood', views.finishgood, name='finishgood'),
    path('displayfinishgoods', views.displayfinishgoods, name='displayfinishgoods'),
    path('displayfinishgoods1', views.displayfinishgoods1, name='displayfinishgoods1'),
    path('delete1/<int:fg_id>/', views.delete_fg, name='delete_fg'),
    path('update1/<int:fg_id>/', views.update_fg, name='update_fg'),
]