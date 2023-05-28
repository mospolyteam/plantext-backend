from rest_framework.viewsets import ModelViewSet

from .models import Book, Review, User
from .serializers import BookSerializer, ReviewSerializer, UserSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
  

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer