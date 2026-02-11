from django.db import models

# Create your models here.
class Category(models.Model):
    CATEGORY_TYPES = [
        ('salads', 'Салати'),
        ('main', 'Основні страви'),
        ('appetizers', 'Закуски'),
        ('soups', 'Супи'),
        ('desserts', 'Десерти'),
        ('drinks', 'Напої'),
        ('breakfast', 'Сніданки'),
    ]

    name = models.CharField(max_length=100, verbose_name="Назва категорії")
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

class Dish(models.Model):
    name = models.CharField(max_length=200, verbose_name="Назва страви")
    category = models.ManyToManyField(Category, related_name='dishes', verbose_name="Категорія")
    price = models.PositiveIntegerField(verbose_name="Ціна")
    is_available = models.BooleanField(default=True, verbose_name="Доступна")
    description = models.TextField(max_length=15000, verbose_name="Опис страви")
    img = models.ImageField(upload_to="dishes" ,verbose_name="Зображення")
    weight = models.PositiveIntegerField(verbose_name="Вага")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Страва"
        verbose_name_plural = "Страви"

