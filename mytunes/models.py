from django.db import models

# Create your models here.

class Album(models.Model):

    title = models.CharField( max_length=300,)
    year_released = models.DateField(auto_now_add=True)
    artist = models.ForeignKey("artist", on_delete=models.CASCADE, related_name="albums")

def _str_(self):
    return self.title


class Artist(models.Model):

    name = models.CharField(max_length=300,)
    genre = models.CharField(max_length=300,)
    bio = models.TextField()
