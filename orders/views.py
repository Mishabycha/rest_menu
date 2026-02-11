from django.shortcuts import render, redirect
from cart.models import CartItem
from .forms import OrderCreateForm
from django.contrib.auth.decorators import login_required
from .models import Order

def order_create(request):
    cart_items = CartItem.objects.filter(user=request.user)
    
    total_price = sum(item.get_total_price() for item in cart_items)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            cart_items.delete()
            return render(request, 'orders/order_created.html', {'order': order})
    else:
        form = OrderCreateForm()

    return render(request, 'orders/order_create.html', {
        'cart_items': cart_items,
        'form': form,
        'total_price': total_price 
    })

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).prefetch_related('items__dish')
    return render(request, 'orders/orders_list.html', {'orders': orders})


