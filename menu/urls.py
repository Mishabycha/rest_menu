from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList, name='menu-list'),
    path('dish/<int:pk>/', views.DishDetail, name='dish-detail'),
]