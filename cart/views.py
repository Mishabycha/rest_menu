from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem
from menu.models import Dish
from django.contrib.auth.decorators import login_required

@login_required
def CartDetail(request):
    items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.get_total_price() for item in items)

    return render(request, 'cart/cart_detail.html', {
        'items': items,
        'total_price': total_price})

@login_required
def CartAdd(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        dish=dish)
    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect('cart:cart-detail')

@login_required
def CartRemove(request, dish_id):
    item = get_object_or_404(
        CartItem,
        user=request.user,
        dish_id=dish_id)
    item.delete()
    return redirect('cart:cart-detail')

