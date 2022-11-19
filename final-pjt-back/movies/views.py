from django.shortcuts import render
import requests
import json
from .models import Movies
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Movies, Reviews
from .serializer import ReviewsSerializer


def movie_list(request):
    movies = Movies.objects.all()
    movies = []
    
    for movie in movies:
        movies.append(
            {
                'id' : movie.pk,
                'movie_id' : movie.movie_id,
                'title' : movie.title,
                'overview' : movie.overview,
                'poster_path' : movie.poster_path,
                'backdrop_path' : movie.backdrop_path,
                'release_date' : movie.release_date,
                'genres' : movie.genres,
                'popularity' : movie.popularity,
                'vote_average' : movie.vote_average,
            }
        )
    return JsonResponse(movies, safe=False)


def movie_detail(request):
    pass
    
def review_create(request):
    pass
    
def detail_review(request):
    pass

def my_review(request, user_pk):
    review_data = get_list_or_404(Reviews)
    serializers = []
    for i in review_data:
        if i.user_id == user_pk:
            review = i
            if request.method == 'GET':
                serializer = ReviewsSerializer(review)
                # print(serializer.data)
                serializers.append(serializer.data)
                
    return JsonResponse(serializers, safe=False)
# @api_view(['GET', 'DELETE', 'PUT'])
# def article_detail(request, article_pk):
#     # article = Article.objects.get(pk=article_pk)
#     article = get_object_or_404(Article, pk=article_pk)

#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         print(serializer.data)
#         return Response(serializer.data)