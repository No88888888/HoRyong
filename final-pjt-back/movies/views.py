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
from .serializer import ReviewsSerializer, WishListSerializer, MoviesSerializer
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

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movies, pk=movie_pk)
    if request.method == 'GET':
        serializer = MoviesSerializer(movie)
        return Response(serializer.data)
    

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
        

# 내 리뷰 수정하는 함수
# 1. 내 프로필의 내 리뷰 페이지에서 리뷰 수정 시 해당 리뷰 수정한 data 수정 후 반환
# 2. 내 프로필의 내 리뷰 페이지에서 리뷰 삭제 시 해당 리뷰 삭제 후 나머지 내 리뷰 반환
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
        # my_review.pop(my_review.index(review))
        review.delete()
        # serializer = ReviewsSerializer(my_review, many=True)
        return Response(status=status.HTTP_204_NO_CONTENT)


# 내 위시리스트 전체 보내주는 함수
# 위시 리스트가 없을 수 있으므로 없으면 빈 리스트 반환
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


# 내 영화 위시 리스트 넣고 빼고 지우는 함수
# 1. 추천페이지에서 위시리스트 토글 클릭 시 위시 리스트에 넣고 뺌
# 2. 내 프로필의 내 위시리스트 화면에서 삭제 시 위시 리스트레서 뺌
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


# 내가 본영화 넣고 빼는 함수
# 내가 본 영화 전체의 movie_id를 담아 프론트에게 전달
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

def recommend_page(request, movie_pk):
    
    pass

import sys
sys.path.append('../')
import krwordrank
from krwordrank.hangle import normalize
from krwordrank.word import KRWordRank



# 리뷰 토크나이저
def get_texts_scores(fname):
    # `fname` 파일은 영화평과 평점이 '&&' 으로 구분된 .txt 파일입니다.
    with open(fname, encoding='utf-8') as f:
        docs = [doc.lower().replace('\n', '').split('&&') for doc in f]
        docs = [doc for doc in docs if len(doc) == 2]
        docs = [doc for doc in docs if len(doc) == 2]

        if not docs:
            return [], []

        texts, scores = zip(*docs)
        return list(texts), list(scores)
    
def get_from_list(l, i, default=('', 0)):
    if len(l) <= i:
        return default
    else:
        return l[i]
    
    
def keyword_extractor():

    beta = 0.85    # PageRank의 decaying factor beta
    max_iter = 10

    top_keywords = []
    # TODO: 유저가 리뷰 작성하는 영화의 리뷰 데이터를 fnames로 가져오기
    fnames = './data/A Werewolf Boy (1).txt'
    
    texts, scores = get_texts_scores(fnames)

    wordrank_extractor = KRWordRank(min_count=5, max_length=10, verbose=False)

    keywords, rank, graph = wordrank_extractor.extract(texts, beta, max_iter)

    top_keywords.append(sorted(keywords.items(), key=lambda x: x[1], reverse=True)[:100])
    top_keywords = sum(top_keywords,[])
    
    
    keyword_counter = {}
    for keywords in top_keywords:
        words, ranks = keywords
        for word in words:
            keyword_counter[word] = keyword_counter.get(word, 0) + 1

    # 커먼키워드 DB에서 가져와서 비교해야함(11.18)
    # TODO: 커먼키워드 DB에서 가져와 set형태로 저장
    common_keywords = {word for word, count in keyword_counter.items()}
    common_keywords = {'송중기', '영화', '정말'}
    selected_top_keywords = []

    for keywords in top_keywords:
        keywords = [keywords]
        # print(keywords)
        for word, r in keywords:
            if word in common_keywords:
                # print(common_keywords)
                continue
            selected_top_keywords.append((word, r))
    # print(selected_top_keywords)
    for k in range(len(selected_top_keywords)):
        res = get_from_list(selected_top_keywords, k)
        # TODO: 산출되서 나온 결과값을 해당 영화 키워드로 저장, 이미 있는 키워드면 가중치를 새로 나온것으로 수정, 없으면 추가
        print(res[0], res[1])


def create_review(request):
    
    pass


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