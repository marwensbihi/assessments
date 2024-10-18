from django.db import models

from .Books import Book
from .Shelfs import Shelf

class BookShelves(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('book', 'shelf')
