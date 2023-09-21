from django.db import models

# Create your models here.
from django.db import models

class Categories(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return f"{self.title} - {self.content} - Category:{self.category}"
    