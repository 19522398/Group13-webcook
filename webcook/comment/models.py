from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=100)
    dish_name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)