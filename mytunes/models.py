from django.db import models

# Create your models here.

class album(models.Model):

    title = models.CharField()
    year_released = models.DateField(auto_now_add=True)
    artist = models.ForeignKey("artist", on_delete=models.CASCADE, related_name="albums")

def _str_(self):
    return self.title

class artist(models.Model):

    name = models.CharField()
    genre = models.CharField()
    bio = models.TextField()
