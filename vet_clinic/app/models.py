from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        unique_together = ('username', 'email')
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Service(models.Model):
    name = models.CharField(max_length=90)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=90)
    phone = models.CharField(unique=True, max_length=20)
    email = models.EmailField(unique=True)
    reception_date = models.DateField(unique=True)
    reception_time = models.DateTimeField(unique=True)


# class contacts(models.Model):  # для фронта как понял
#     addres = models.CharField(max_length=120)
#     work_time = models.CharField(max_length=30)
#     phone = models.CharField(unique=True, max_length=20)
#     email = models.EmailField(unique=True)
# social_links = models. подумай как релаизовать


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Отзыв был оставлен пользователем: {self.user.name}"
