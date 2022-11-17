from django.db import models
from django.conf import settings

# Create your models here.

class Movies(models.Model):
    movie_id = models.IntegerField()
    title = models.TextField()
    poster_path = models.TextField()
    backdrop_path = models.TextField()
    overview = models.TextField()
    release_date = models.DateField()
    genre_ids = models.IntegerField()
    popularity = models.IntegerField()
    vote_average = models.IntegerField()
    
class Reviews(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    title = models.TextField()
    sentense = models.TextField()
    score = models.FloatField()

class WishList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    title = models.TextField()
    poster_path = models.TextField()

class Keyword(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    keyword = models.TextField()
    keyword_score = models.FloatField()