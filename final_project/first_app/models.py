from django.db import models


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=128)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    rating = models.IntegerField()
    released = models.DateField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.genre}"
