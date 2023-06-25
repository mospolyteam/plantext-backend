from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.cache import cache

from .models import Book, Review, User, Writer
from .serializers import BookSerializer, ReviewSerializer, UserSerializer, WriterSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request):
        if cache.ttl('books'):
            queryset = cache.get('books')
        else:
            queryset = Book.objects.all()
            cache.set('books', queryset, 60)
        serializer = BookSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

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


class WriterViewSet(ModelViewSet):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer