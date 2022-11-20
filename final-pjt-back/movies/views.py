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

@api_view(['GET'])
def my_review(request, user_pk):
    review_data = get_list_or_404(Reviews)
    serializers = []
    if request.method == 'GET':
        for review in review_data:
            if review.user_id == user_pk:
                serializer = ReviewsSerializer(review)
                # print(serializer.data)
                serializers.append(serializer.data)
    return JsonResponse(serializers, safe=False)
        


@api_view(['PUT', 'DELETE'])
def modify_myreview(request, user_pk, movie_pk):
    review_data = get_list_or_404(Reviews)
    my_review = []
    for review in review_data:
        if review.user_id == user_pk:
            my_review.append(review)
            
    if request.method == 'PUT':
        review = Reviews.objects.get(user_id=user_pk, movie_id=movie_pk)
        serializer = ReviewsSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        review = Reviews.objects.get(user_id=user_pk, movie_id=movie_pk)
        my_review.pop(my_review.index(review))
        review.delete()
        serializer = ReviewsSerializer(my_review, many=True)
        return Response(serializer.data)



@api_view(['GET'])
def wish_list(request):
    wishlist_data = WishList.objects.all()
    serializers = []
    if request.method == 'GET':
        for wishlist in wishlist_data:
            if wishlist.user_id == request.user.pk:
                serializer = WishListSerializer(wishlist)
                # print(serializer.data)
                serializers.append(serializer.data)
        else:        
            return JsonResponse(wishlist_data, safe=False)
    return JsonResponse(serializers, safe=False)

@csrf_exempt
@api_view(['POST', 'DELETE'])
def modify_wishlist(request, movie_pk):
    request.user.pk = 1
    wishlist = WishList.objects.all()
    my_wish_movie = []
    for i in wishlist:
        if i.user_id == request.user.pk:
            my_wish_movie.append(i)
    # print(my_wish_movie)
    if request.method == 'POST':
        for i in wishlist:
            if i.movie_id == movie_pk and i.user_id == request.user.pk:
                delete_id= i.id
                wishmovie = get_object_or_404(WishList, pk=delete_id)
                my_wish_movie.pop(my_wish_movie.index(wishmovie))
                wishmovie.delete()
                break
        else:
            added_wish_movie = WishList(
                user_id = request.user.pk,
                movie_id = movie_pk
            )
            added_wish_movie.save()
            my_wish_movie.append(added_wish_movie)
            print('1',my_wish_movie)
    elif request.method == 'DELETE':
        wishmovie = WishList.objects.get(movie_id=movie_pk, user_id=request.user.pk)
        my_wish_movie.pop(my_wish_movie.index(wishmovie))
        # print('2', my_wish_movie)
        wishmovie.delete()
    serializer = WishListSerializer(my_wish_movie, many=True)
    return Response(serializer.data)


# 내가 본영화 넣고 빼고 함수
# 프론트에게 내가 본 영화 전체의 movie_id를 담아 전달
@csrf_exempt
@require_POST
def watched_movie(request, movie_pk):
    if request.user.is_authenticated:
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

# @api_view(['GET'])
# def wish_list(request, user_pk):
#     wishlist_data = get_list_or_404(WishList)
#     serializers = []
#     for i in wishlist_data:
#         if i.user_id == user_pk:
#             wishlist = i
#             if request.method == 'GET':
#                 serializer = WishListSerializer(wishlist)
#                 # print(serializer.data)
#                 serializers.append(serializer.data)
#             # if request.method == 'DELETE':
#             #     # .remove('해당무비')
#             #     pass
#     return JsonResponse(serializers, safe=False)