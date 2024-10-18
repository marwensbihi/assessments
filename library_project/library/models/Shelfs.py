from django.db import models
from django.contrib.auth.models import User

class Shelf(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shelves')

    def __str__(self):
        return self.shelf_name
