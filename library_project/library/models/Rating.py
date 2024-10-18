from django.db import models
from django.contrib.auth.models import User

from .Books import Book


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.FloatField()
    review = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} - {self.book.title} ({self.rating})'
