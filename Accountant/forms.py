from django import forms
from .models import Payment_paid
from Inventory.models import Purchase_Party

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment_paid
        fields = ['purchase_party', 'paid_date', 'amt_paid']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add any additional customization here if needed
        # For example, you can customize widget attributes:
        self.fields['purchase_party'].widget.attrs.update({'class': 'form-control'})
        self.fields['paid_date'].widget.attrs.update({'class': 'form-control', 'type': 'date'})
        self.fields['amt_paid'].widget.attrs.update({'class': 'form-control'})

        # Query Purchase_Party to get all parties for dropdown
        self.fields['purchase_party.name'].queryset = Purchase_Party.objects.all()
