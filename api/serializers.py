from .models import Book, Review, User
from rest_framework import serializers


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['url', 'name', 'author', 'description', 'image', 'reading_count', 'reviews_count', 'quotes_count',
                  'rating']


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ['url', 'book', 'user', 'text_review', 'created_at']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'last_login', 'first_name', 'last_name', 'email', 'photo', 'bio', 'is_active', 'is_staff',
                  'is_superuser']
        read_only_field = ['is_active', 'is_staff', 'is_superuser']
