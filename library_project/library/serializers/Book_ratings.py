# serializers/book_ratings.py
from rest_framework import serializers
from ..models.Book_ratings import BookRating

class BookRatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRating
        fields = '__all__'
