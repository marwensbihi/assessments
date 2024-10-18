# serializers/book_shelves.py
from rest_framework import serializers
from ..models import BookShelves

class BookShelvesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookShelves
        fields = '__all__'
