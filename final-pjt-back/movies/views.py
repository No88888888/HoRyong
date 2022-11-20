from django.shortcuts import render
import requests
import json
from .models import Movies, WishList
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
# permission Decorators
from rest_framework.decorators import permission_classes
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from rest_framework.permissions import IsAuthenticated
from .models import Movies, Reviews, WatchedMovie, WishList
from .serializer import ReviewsSerializer, WishListSerializer
from django.views.decorators.csrf import csrf_exempt



def movie_list(request):
    movies = Movies.objects.all()
    movies_list = []
    for movie in movies:
        movies_list.append(
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
    return JsonResponse(movies_list, safe=False)


def movie_detail(request):
    pass
    
def create_review(request):
    pass
    
# def detail_review(request):
#     pass

@api_view(['GET', 'PUT', 'DELETE'])
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
                
            if request.method == 'PUT':
                pass
    return JsonResponse(serializers, safe=False)


@api_view(['GET', 'POST'])
def wish_list(request, user_pk):
    wishlist_data = get_list_or_404(WishList)
    serializers = []
    for i in wishlist_data:
        if i.user_id == user_pk:
            wishlist = i
            if request.method == 'GET':
                serializer = WishListSerializer(wishlist)
                # print(serializer.data)
                serializers.append(serializer.data)
            # if request.method == 'DELETE':
            #     # .remove('해당무비')
            #     pass
    return JsonResponse(serializers, safe=False)


# 내가 본영화 넣고 빼고 함수
# 프론트에게 내가 본 영화 전체의 movie_id를 담아 전달
@csrf_exempt
@require_POST
def watched_movie(request, movie_pk):
    request.user.pk = 1
    watchedmovie = WatchedMovie.objects.all()
    my_watch_movie = []
    for i in watchedmovie:
        if i.user_id == request.user.pk:
            my_watch_movie.append(i.movie_id)
    for i in watchedmovie:
        if i.movie_id == movie_pk and i.user_id == request.user.pk:
            delete_id= i.id
            watchmovie = get_object_or_404(WatchedMovie, pk=delete_id)
            watchmovie.delete()
            my_watch_movie.remove(movie_pk)
            break
    else:
        added_watched_movie = WatchedMovie(
            user_id = request.user.pk,
            movie_id = movie_pk
        )
        added_watched_movie.save()
        my_watch_movie.append(added_watched_movie.movie_id)
    return JsonResponse(my_watch_movie, safe=False)


# TODO: 위시리스트 어덯게 해야하지
# @require_POST
# def follow(request, movie_pk):
#     if request.user.is_authenticated:
#         User = get_user_model()
#         me = request.user
#         you = User.objects.get(pk=user_pk)
#         if me != you:
#             # 내가 (request.user) 그 사람의 팔로워 목록에 있다면
#             # if me in you.followers.all():
#             if you.followers.filter(pk=me.pk).exists():
#                 #언팔로우
#                 you.followers.remove(me)
#             else:
#                 # 팔로우
#                 you.followers.add(me)
#         return redirect('accounts:profile', you.username)
#     return redirect('accounts:login')





# @api_view(['GET', 'DELETE', 'PUT'])
# def article_detail(request, article_pk):
#     # article = Article.objects.get(pk=article_pk)
#     article = get_object_or_404(Article, pk=article_pk)

#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         print(serializer.data)
#         return Response(serializer.data)