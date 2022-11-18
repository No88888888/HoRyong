from django.db import models
from django.conf import settings

# Create your models here.

class Movies(models.Model):
    movie_id = models.IntegerField()
    title = models.TextField()
    poster_path = models.TextField()
    backdrop_path = models.TextField(null=True)
    overview = models.TextField(blank=True)
    release_date = models.DateField(blank=True)
    genres = models.TextField()
    popularity = models.IntegerField()
    vote_average = models.IntegerField()
    
class Reviews(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'user_reviews')
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name = 'movie_reviews')
    sentence = models.TextField()
    score = models.FloatField()

class WishList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'user_wishlist')
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name = 'movie_wishlist')

class Keyword(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name = 'movie_keyword')
    keyword = models.TextField()
    keyword_score = models.FloatField()

class CommonKeyword(models.Model):
    common_keyword = models.TextField()
    
class WatchedMovie(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'user_watchedmovie')
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name = 'movie_watchedmovie')