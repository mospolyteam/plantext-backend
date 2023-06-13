from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="Email", unique=True)
    first_name = models.CharField(verbose_name="Имя", max_length=255)
    last_name = models.CharField(verbose_name="Фамилия", max_length=255)
    photo = models.ImageField(verbose_name="Аватарка", upload_to="users/photos",
                              default="../static/images/avatar-placeholder.svg")
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
    book = models.ForeignKey(to='Book', verbose_name='Книга', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    is_published = models.BooleanField(verbose_name='Опубликован', default=False)

    def __str__(self):
        return self.text_review[:32]

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Quote(models.Model):
    author = models.ForeignKey(to=User, verbose_name='Автор', on_delete=models.SET_NULL, null=True)
    text = models.TextField(verbose_name='Текст цитаты')
    book = models.ForeignKey(to='Book', verbose_name='Книга', on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    is_published = models.BooleanField(verbose_name='Опубликова', default=False)

    def __str__(self):
        return f'{self.text[:16]}... | {self.book}'

    class Meta:
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитаты'


class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    author = models.CharField(max_length=255, verbose_name='Автор')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Обложка', upload_to='books/previews')
    reading = models.ManyToManyField(to=User, verbose_name='Прочтения', related_name='readings')
    ratings = models.ManyToManyField(to=User, through='BookRatingRelationship', related_name='book_ratings')

    @property
    def reading_count(self):
        return self.reading.count()

    reading_count.fget.short_description = 'Количество прочтений'

    @property
    def reviews_count(self):
        return self.review_set.count()

    reviews_count.fget.short_description = 'Количество отзывов'

    @property
    def quotes_count(self):
        return self.quote_set.count()

    quotes_count.fget.short_description = 'Количество цитат'

    @property
    def rating(self):
        return self.ratings.count()

    rating.fget.short_description = 'Оценка'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class BookRatingRelationship(models.Model):
    book = models.ForeignKey(to=Book, verbose_name='Книга', on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, verbose_name='Автор', on_delete=models.SET_NULL, null=True)
    value = models.IntegerField(verbose_name='Оценка')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'


class Article(models.Model):
    title = models.CharField(max_length=64, verbose_name='Заголовок')
    author = models.ForeignKey(to=User, verbose_name='Автор', null=True, blank=True, on_delete=models.SET_NULL)
    text = models.TextField(verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Writer(models.Model):
    name = models.CharField(max_length=64, verbose_name='ФИО')
    birthday = models.DateField(verbose_name='Дата рождения')
    death_day = models.DateField(verbose_name='Дата смерти')
    ratings = models.ManyToManyField(to=User, through='WriterRatingRelationship', related_name='writer_ratings')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class WriterRatingRelationship(models.Model):
    writer = models.ForeignKey(to=Writer, verbose_name='Писатель', on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, verbose_name='Автор', on_delete=models.SET_NULL, null=True)
    value = models.IntegerField(verbose_name='Оценка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Оценка автора'
        verbose_name_plural = 'Оценки авторов'


class Partner(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    image = models.ImageField(verbose_name='Логотип', upload_to='partners')
    link = models.CharField(max_length=128, verbose_name='Ссылка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'
