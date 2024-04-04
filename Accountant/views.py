from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from Inventory.models import *
from Accountant.models import *
from .models import Purchase_Party, Payment_paid
from .forms import PaymentForm

def make_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            purchase_party = form.cleaned_data['purchase_party']
            paid_date = form.cleaned_data['paid_date']
            amt_paid = form.cleaned_data['amt_paid']

            # Create Payment_paid object and save to database
            payment = Payment_paid(
                purchase_party=purchase_party,
                purchase_party_name=purchase_party.name,
                paid_date=paid_date,
                amt_paid=amt_paid
            )
            payment.save()

            # Redirect to a success page or wherever needed
            return redirect('payment_success')
    else:
        form = PaymentForm()

    return render(request, 'make_payment.html', {'form': form})

def payment_success(request):
    return render(request, 'payment_success.html')
#---------------purchasebill---------------
def purchasebill(request):
    purchase=Purchase_Party.objects.all()
    raw=RawMaterial.objects.all()
    return render(request,"purchasebill.html",{
        'purchase':purchase,
        'raw':raw
    })
def displaypurchasebill(request):
    n = request.POST.get('clickcount')
    date = request.POST.get('date')
    p_id = request.POST.get('p_name')
    total_amount = 0
    p1 = Purchase_Party.objects.get(id=p_id)
    p2 = PurchaseBill.objects.create(party=p1, date_of_genrate=date, Totall_amt=total_amount)

    for i in range(int(n)):
        r_name = request.POST.get('r_name' + str(i))
        piece = request.POST.get('piece' + str(i))
        amount = request.POST.get('amount' + str(i))
        total_amount += int(piece) * int(amount)

        if  purchase_item.objects.filter(purchase=p2, RM_name=r_name).exists():
            i1 = Inventory.objects.get(Item_name=r_name)
            i1.Item_qty += int(piece)
            i1.save()
            p3 = purchase_item.objects.get(RM_name=r_name, purchase=p2, inventory=i1)
            p3.RM_qty += int(piece)
            p3.save()
        else:
            p3 = purchase_item(RM_name=r_name, RM_qty=piece, RM_price=amount, purchase=p2)
            p3.save()

    p2.Totall_amt = total_amount
    p2.save()
    return redirect("displaypurchasebill1")

        
from django.shortcuts import render
from .models import purchase_item

def displaypurchasebill1(request):
    # Get all purchase items
    purchase_items = purchase_item.objects.all() 
    
    # Dictionary to store unique bills and corresponding items
    unique_bills = {}

    # Iterate through purchase items to group them by purchase bill ID and calculate subtotal
    for item in purchase_items:
        if item.purchase.id not in unique_bills:
            unique_bills[item.purchase.id] = {
                'bill_id': item.id,
                'party_name': item.purchase.party.name,
                'date_of_genrate': item.purchase.date_of_genrate,
                'total_amount': item.purchase.Totall_amt,
                'items': [],
                'subtotal': 0  # Initialize subtotal for each bill
            }

        # Calculate subtotal for each item and add it to the bill's subtotal
        subtotal_item = item.RM_qty * item.RM_price
        unique_bills[item.purchase.id]['subtotal'] += subtotal_item

        # Add item details to the bill's items list
        unique_bills[item.purchase.id]['items'].append({
            'RM_name': item.RM_name,
            'RM_qty': item.RM_qty,
            'RM_price': item.RM_price,
            'subtotal_item': subtotal_item  # Include subtotal for the item
        })

    # Convert the dictionary values to a list for easier iteration in the template
    purchase_bill_list = list(unique_bills.values())

    return render(request, "displaypurchasebill.html", {
        'purchase_bill_list': purchase_bill_list,
    })

#--------------------------sales bill
    
    
def salesbill(request):
    sellers=Sales_Party.objects.all()
    products=FinishGoods.objects.all()
    print(products)
    return render(request,"salesbill.html",{
        'sellers':sellers,
        'products':products
    })
def displaysalesbill(request):
    n = request.POST.get('clickcount')
    date = request.POST.get('date')
    p_id = request.POST.get('seller')
    total_amount = 0
    p1 = Sales_Party.objects.get(id=p_id)
    p2 = SalesBill.objects.create(party=p1, date_of_genrate=date, Totall_amt=total_amount)

    for i in range(int(n)):
        r_name = request.POST.get('product' + str(i))
        piece = request.POST.get('piece' + str(i))
        amount = request.POST.get('amount' + str(i))
        total_amount += int(piece) * int(amount)

        if Inventory.objects.filter(Item_name=r_name).exists() and sales_item.objects.filter(sales=p2, FG_name=r_name).exists():
            i1 = Inventory.objects.get(Item_name=r_name)
            i1.Item_qty += int(piece)
            i1.save()
            p3 = sales_item.objects.get(FG_name=r_name, sales=p2, inventory=i1)
            p3.FG_qty += int(piece)
            p3.save()
        elif Inventory.objects.filter(Item_name=r_name).exists():
            i1 = Inventory.objects.get(Item_name=r_name)
            i1.Item_qty += int(piece)
            i1.save()
            p3 = sales_item(FG_name=r_name, FG_qty=piece, FG_price=amount, sales=p2, inventory=i1)
            p3.save()
        else:
            i1 = Inventory(Item_name=r_name, Item_qty=piece)
            i1.save()
            p3 = sales_item(FG_name=r_name, FG_qty=piece, FG_price=amount, sales=p2, inventory=i1)
            p3.save()

    p2.Totall_amt = total_amount
    p2.save()
    return redirect("displaysalesbill1")
def displaysalesbill1(request):
    # Get all purchase items
    purchase_items = sales_item.objects.all()

    # Dictionary to store unique bills and corresponding items
    unique_bills = {}

    # Iterate through purchase items to group them by purchase bill ID
    for item in purchase_items:
        if item.sales.id not in unique_bills:
            unique_bills[item.sales.id] = {
                'bill_id': item.id,
                'party_name': item.sales.party.name,
                'date_of_genrate': item.sales.date_of_genrate,
                'total_amount': item.sales.Totall_amt,
                'items': []
            }

        unique_bills[item.sales.id]['items'].append({
            'FG_name': item.FG_name,
            'FG_qty': item.FG_qty,
            'FG_price': item.FG_price
        })

    # Convert the dictionary values to a list for easier iteration in the template
    purchase_bill_list = list(unique_bills.values())

    return render(request, "displaysalesbill.html", {
        'purchase_bill_list': purchase_bill_list,
    })
            
#------------inventory


def display_inventory(request):
    inventory_items = Inventory.objects.all()
    return render(request, "display_inventory.html", {'inventory_items': inventory_items})
def paymentreceived(request):
    return render(request,"paymentreceived.html")
def paymentpaid(request):
    purchase_parties=Purchase_Party.objects.all()
    return render(request,"payment_paid.html",{
        'purchase_parties':purchase_parties
    })
def creditors(request):
    return render(request,"creditors.html")
def debtors(request):
    return render(request,"debtors.html")
def Misc(request):
     return render(request,"miscelleneousexpanse.html")


def payment_paid(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        party_id = request.POST.get('party_id')
        paid_date = request.POST.get('paid_date')
        amt_paid = request.POST.get('amt_paid')

        # Retrieve the purchase party
        purchase_party = PurchaseBill.objects.get(id=party_id)

        # Calculate the remaining amount
        remaining_amt = purchase_party.Totall_amt - float(amt_paid)

        # Create Payment_paid instance
        payment = Payment_paid.objects.create(
            date=date,
            purchase_party=purchase_party,
            purchase_party_name=purchase_party.party.name,
            paid_date=paid_date,
            amt_paid=amt_paid
        )

        # Update remaining amount in PurchaseBill
        purchase_party.remaining_amt = remaining_amt
        purchase_party.save()

        # Redirect to payment success page
        return redirect('payment_success')

    return render(request, 'payment_paid.html')

def payment_success(request):
    return render(request, 'payment_success.html')
