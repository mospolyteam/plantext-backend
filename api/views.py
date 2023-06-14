from rest_framework.viewsets import ModelViewSet
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Book, Review, User
from .serializers import BookSerializer, ReviewSerializer, UserSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @receiver(post_save)
    def send_mail_on_create(sender, instance=None, created=False, **kwargs):
        if created:
            if (sender == Book):
                send_mail(
                    "New book",
                    "We have a new book",
                    "plantext@bookshop.ru",
                    ["examplemail@mail.com"],
                    fail_silently=False,
                )


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
