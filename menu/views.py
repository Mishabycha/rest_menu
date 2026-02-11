from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from .forms import DishForm, CategoryForm, DishFilterForm
from .models import Category, Dish

def MenuList(request):
    categories = Category.objects.filter(is_active=True)
    dishes = Dish.objects.filter(is_available=True)

    category_id = request.GET.get('category')
    if category_id:
        dishes = dishes.filter(category__id=category_id)

    query = request.GET.get('q')
    if query:
        dishes = dishes.filter(name__icontains=query)

    return render(request, 'menu/menu.html', {
        'categories': categories,
        'dishes': dishes
    })

def DishDetail(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    return render(request, 'menu/dish_detail.html', {'dish': dish})