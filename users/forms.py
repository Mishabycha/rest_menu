from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(required=False, label="Логін",
                            widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(required=True, label="Email", widget=forms.EmailInput(attrs={"class": "form-control"})),
    first_name = forms.CharField(required=False, label="Ім'я",
                            widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(required=False, label="Прізвище",
                            widget=forms.TextInput(attrs={"class": "form-control"}))
    

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
        
class ProfileRegisterForm(forms.ModelForm):
    date_of_birth = forms.DateField(required=False, label="Дата народження",
                                    widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}))
    avatar = forms.ImageField(required=False, label="Аватар")
    phone = forms.CharField(required=False, label="Номер телефону",
                            widget=forms.TextInput(attrs={"class": "form-control"}))
    adress = forms.CharField(required=False, label="Адреса",
                            widget=forms.TextInput(attrs={"class": "form-control"}))
    

    class Meta:
        model = Profile
        fields = ("date_of_birth", "avatar", "phone", "adress")


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Логін",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("date_of_birth", "avatar", "phone", "address")
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "avatar": forms.FileInput(attrs={"required": False, "label": "Аватар"})
        }