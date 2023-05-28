from rest_framework.viewsets import ModelViewSet

from .models import Book, Review
from .serializers import BookSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer