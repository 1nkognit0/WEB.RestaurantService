from django.shortcuts import render

from orders.models import Menu

def create_order(request):
    menu_data = Menu.objects.all()
    return render(request, 'orders/waiter.html', {'menu': menu_data})