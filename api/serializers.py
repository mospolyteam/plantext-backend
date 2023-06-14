from .models import Book, Review, User, Quote, BookRatingRelationship, Article, Writer, WriterRatingRelationship, \
    Partner
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


class QuoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'


class BookRatingRelationshipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookRatingRelationship
        fields = '__all__'


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class WriterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Writer
        fields = '__all__'


class WriterRatingRelationshipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WriterRatingRelationship
        fields = '__all__'


class PartnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'
