from django import forms

from orders.models import Order, Menu, OrderItem

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['table_number']

