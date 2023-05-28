from rest_framework.viewsets import ModelViewSet

from .models import Book, Review
from .serializers import BookSerializer, ReviewSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer