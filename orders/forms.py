from django import forms

from orders.models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['table_number']

