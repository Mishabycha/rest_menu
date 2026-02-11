from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Дата народження")
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name="Аватар")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")
    address = models.CharField(max_length=55, verbose_name="Адреса")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = "Профіль"
        verbose_name_plural = "Профілі"

    def __str__(self):
        return self.user.username
    
    
