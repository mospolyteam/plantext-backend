from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="Email", unique=True)
    first_name = models.CharField(verbose_name="Имя", max_length=255)
    last_name = models.CharField(verbose_name="Фамилия", max_length=255)
    photo = models.ImageField(verbose_name="Аватарка", upload_to="users/photos", default="../static/images/avatar-placeholder.svg")
    bio = models.TextField(verbose_name="О себе", blank=True)

    is_active = models.BooleanField(verbose_name='Активирован', default=True)
    is_staff = models.BooleanField(verbose_name='Персонал', default=False)
    is_superuser = models.BooleanField(verbose_name='Администратор', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Review(models.Model):
    user = models.ForeignKey(to=User, verbose_name='Автор отзыва', on_delete=models.PROTECT)
    text_review = models.TextField(verbose_name="Текст отзыва")

    def __str__(self):
        return self.text_review[:32]
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    author = models.CharField(max_length=255, verbose_name='Автор')
    description = models.TextField(verbose_name='Описание')
    reviews = models.ForeignKey(to=Review, verbose_name="Отзывы", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'