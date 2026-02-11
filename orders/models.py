from django.db import models
from django.contrib.auth.models import User
from menu.models import Dish

class Order(models.Model):
    PAYMENT_CHOICES = [
        ('CASH', 'Готівка при отриманні'),
        ('ONLINE', 'Онлайн оплата'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    first_name = models.CharField(max_length=50, verbose_name="Ім'я")
    last_name = models.CharField(max_length=50, verbose_name="Прізвище")
    email = models.EmailField()
    address = models.CharField(max_length=250, verbose_name="Адреса доставки")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False, verbose_name="Оплачено")
    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default='CASH')

    class Meta:
        ordering = ['-created']
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"

    def __str__(self):
        return f'Замовлення {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
