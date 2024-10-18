from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, blank=True, null=True)
    image_url = models.URLField(max_length=255, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    fans_count = models.IntegerField(default=0)
    ratings_count = models.IntegerField(default=0)
    average_rating = models.FloatField(default=0.0)
    text_reviews_count = models.IntegerField(default=0)
    works_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name
