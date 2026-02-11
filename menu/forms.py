from django.forms import ModelForm, TextInput, Textarea, Select, FileInput, NumberInput, Form
from .models import Category, Dish

class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = ["name", "category", "price", "is_available", "description", "img", "weight"]

        widgets = {
            "name": TextInput(attrs={"class": "form-control", "placeholder": "Страва", "required": True}),
            "description": Textarea(attrs={"class": "form-control", "placeholder": "Опис страви", "required": True}),
            "price": NumberInput(attrs={"class": "form-control", "placeholder": "Ціна", "required": True}),
            "is_available": Select(attrs={"class": "form-control", "placeholder": "Доступно", "required": True}),
            "img": FileInput(attrs={"class": "form-control", "placeholder": "Зображення", "required": True}),
            "weight": NumberInput(attrs={"class": "form-control", "placeholder": "Вага", "required": True}),

        }

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name", "is_active"]

        widgets = {
            "name": TextInput(attrs={"class": "form-control", "placeholder": "Категорія", "required": True}),
            "is_active": Select(attrs={"class": "form-control", "placeholder": "Доступно", "required": True}),
        }

class DishFilterForm(Form):
    CATEGORY_TYPES = [
        ('salads', 'Салати'),
        ('main', 'Основні страви'),
        ('appetizers', 'Закуски'),
        ('soups', 'Супи'),
        ('desserts', 'Десерти'),
        ('drinks', 'Напої'),
        ('breakfast', 'Сніданки'),
    ]