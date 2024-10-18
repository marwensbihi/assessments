from django.db import models

from .Authors import Author

class Work(models.Model):
    work_id = models.CharField(max_length=20, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    ratings_count = models.IntegerField(default=0)
    average_rating = models.FloatField(default=0.0)
    text_reviews_count = models.IntegerField(default=0)

    def __str__(self):
        return self.work_id
