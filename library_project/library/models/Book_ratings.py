from django.db import models

from .Books import Book

class BookRating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.IntegerField()  # This could be a ForeignKey to a User model if you have one
    rating = models.IntegerField()
    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Rating for {self.book.title} by User {self.user_id}'
