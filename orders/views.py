from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import functools

from orders.models import Menu, OrderItem, Order
from orders.forms import OrderForm

def role_required(allowed_role):
    def decorator(view_func):
        @functools.wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.user.role != allowed_role:
                return HttpResponseForbidden("Доступ запрещён для вашей роли!")
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator

@login_required
@role_required('waiter')
def create_order(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save()
            order_items = []

            for item_number in range(int(request.POST.get('itemCount'))):
                dish_id = request.POST.get(f'item-{item_number}')
                quantity = request.POST.get(f'quantity-{item_number}')

                item = OrderItem.objects.create(dish_id_id=dish_id, order_id=order,  quantity=quantity)

                order_items.append({
                    'name': item.dish_id.name,
                    'quantity': item.quantity
                })

            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "orders",
                {
                    "type": "new_order",
                    "data": {
                        "order": {
                            "id": order.id,
                            "table_number": order.table_number,
                            "items": order_items
                        }
                    }
                }
            )

            return redirect(request.META.get('HTTP_REFERER'))
    else:
        order_form = OrderForm()
    menu = Menu.objects.all()
    return render(request, 'orders/waiter.html', {
        'order_form': order_form,
        'menu': menu,
    })

@login_required
@role_required('chef')
def view_orders(request):
    orders = Order.objects.all().prefetch_related('orderitem_set__dish_id')
    data = [{'id': order.id,
             'table_number': order.table_number,
             'order_positions': [{
                        'name': position.dish_id.name,
                        'quantity': position.quantity,
             } for position in order.orderitem_set.all()]

    } for order in orders]
    return render(request, 'orders/chef.html', {'orders': data})