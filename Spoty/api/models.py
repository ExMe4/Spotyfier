from django.db import models

# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=600, default="")
    artist = models.CharField(max_length=600, default="")
    album = models.CharField(max_length=600, default="")
    duration = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, max_length=5000)

    #def is_song_podcast(duration)

class Playlist(models.Model):
    Song
