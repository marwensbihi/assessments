# serializers/book_authors.py
from rest_framework import serializers
from ..models import BookAuthors

class BookAuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAuthors
        fields = '__all__'
