from django.shortcuts import render, redirect

from orders.models import Menu, OrderItem
from orders.forms import OrderForm

def create_order(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save()
            for item_number in range(int(request.POST.get('itemCount'))):
                dish_id = request.POST.get(f'item-{item_number}')
                quantity = request.POST.get(f'quantity-{item_number}')

                OrderItem.objects.create(dish_id_id=dish_id, order_id=order,  quantity=quantity)

            return redirect(request.META.get('HTTP_REFERER'))
    else:
        order_form = OrderForm()
    menu = Menu.objects.all()
    return render(request, 'orders/waiter.html', {
        'order_form': order_form,
        'menu': menu,
    })

def view_orders(request):
    return render(request, 'orders/chef.html')