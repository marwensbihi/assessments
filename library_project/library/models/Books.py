from django.db import models

from .Series import Series
from .Works import Work
from .Authors import Author

class Book(models.Model):
    book_id = models.CharField(max_length=20, unique=True)
    work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, blank=True, null=True, unique=True)
    isbn13 = models.CharField(max_length=13, blank=True, null=True, unique=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    average_rating = models.FloatField(default=0.0)
    ratings_count = models.PositiveIntegerField(default=0)
    text_reviews_count = models.PositiveIntegerField(default=0)
    publication_date = models.DateField(blank=True, null=True)
    original_publication_date = models.DateField(blank=True, null=True)
    format = models.CharField(max_length=50, blank=True, null=True)
    edition_information = models.CharField(max_length=100, blank=True, null=True)
    image_url = models.URLField(max_length=255, blank=True, null=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)
    num_pages = models.PositiveIntegerField(default=0)
    series = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True, related_name='books')
    series_position = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    authors = models.ManyToManyField(Author, related_name='books')

    def __str__(self):
        return self.title
