from django.contrib import admin
from django.urls import path
from . import views

app_name= "cart"

urlpatterns = [
    path('', views.CartDetail, name='cart-detail'),
    path('add/<int:dish_id>/', views.CartAdd, name='cart-add'),
    path('remove/<int:dish_id>/', views.CartRemove, name='cart-remove'),   
    ]