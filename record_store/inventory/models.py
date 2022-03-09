from django.db import models

# All classess

class Artist(models.Model):
    name = models.CharField(max_length=255)

    # Identifier for the object
    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    stock_level = models.IntegerField()
    # fk coming from Artist
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title