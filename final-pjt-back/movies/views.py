import random
import sys
sys.path.append('../')

from django.http.response import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
# permission Decorators
from rest_framework.decorators import api_view
from rest_framework.response import Response

import krwordrank
from krwordrank.hangle import normalize
from krwordrank.word import KRWordRank

from .models import (CommonKeyword, Keyword, Movies, Reviews, WatchedMovie, WishList)
from .serializer import (KeywordsSerializer, MoviesSerializer, ReviewsSerializer, WishListSerializer)

# 영화 정보 전체 반환 함수
@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movies)
    if request.method == 'GET':
        serializer = MoviesSerializer(movies, many=True)
        return Response(serializer.data)

# 영화 디테일 정보 반환 함수
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movies, pk=movie_pk)
    if request.method == 'GET':
        serializer = MoviesSerializer(movie)
        return Response(serializer.data)

# 영화별 리뷰 전체 반환 함수
@api_view(['GET'])
def movie_review(request, movie_pk):
    review_data = get_list_or_404(Reviews)
    reviews = []
    if request.method == 'GET':
        for review in review_data:
            if review.movie_id == movie_pk:
                reviews.append(review)
        serializer = ReviewsSerializer(reviews, many=True)
        return Response(serializer.data)

# 내가 작성한 리뷰 전체 반환 함수
@api_view(['GET'])
def my_review(request, user_pk):
    review_data = get_list_or_404(Reviews)
    serializers = []
    if request.method == 'GET':
        for review in review_data:
            if review.user_id == user_pk:
                serializer = ReviewsSerializer(review)
                serializers.append(serializer.data)
    return JsonResponse(serializers, safe=False)


# 내 리뷰 수정 함수
# PUT - 내 프로필의 내 리뷰 페이지에서 리뷰 수정 시 해당 리뷰 수정한 data 수정 후 반환
# DELETE - 내 프로필의 내 리뷰 페이지에서 리뷰 삭제 시 해당 리뷰 삭제 후 나머지 내 리뷰 반환
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


# 내 위시리스트 전체 반환 함수
# 위시 리스트가 없을 시 빈 리스트 반환
@api_view(['GET'])
def wish_list(request, user_pk):
    wishlist_data = WishList.objects.all()
    serializers = []
    if request.method == 'GET':
        for wishlist in wishlist_data:
            if wishlist.user_id == user_pk:
                serializer = WishListSerializer(wishlist)
                serializers.append(serializer.data)
        else:
            return JsonResponse(serializers, safe=False)
    return JsonResponse(serializers, safe=False)

# 내 위시리스트 추가, 삭제 함수
# POST - 내 위시리스트에 있을 시 삭제, 없을 시 추가
# DELETE - 내 위시리스트에서 삭제
@api_view(['POST', 'DELETE'])
def modify_wishlist(request, movie_pk, user_pk):
    wishlist = WishList.objects.filter(user_id=user_pk, movie_id=movie_pk)
    if request.method == 'POST':
        if wishlist:
            wishlist.delete()
        else:
            added_wish_movie = WishList(
                user_id=user_pk,
                movie_id=movie_pk
            )
            added_wish_movie.save()
        wishlists = WishList.objects.all()
        serializer = WishListSerializer(wishlists, many=True)
        return Response(serializer.data)
    if request.method == 'DELETE':
        wishlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 내 본영화 전체 반환 함수
@api_view(['GET'])
def get_watched_movie(request):
    if request.user.is_authenticated:
        watchedmovie_data = WatchedMovie.objects.all()
        my_watch_movie = []
        for watchedmovie in watchedmovie_data:
            if watchedmovie.user_id == request.user.pk:
                my_watch_movie.append(watchedmovie.movie_id)
        return JsonResponse(my_watch_movie, safe=False)


# 내가 본영화 추가, 삭제 후 반환 함수
@api_view(['POST'])
def watched_movie(request, movie_pk):
    if request.user.is_authenticated:
        watchedmovie = WatchedMovie.objects.all()
        my_watch_movie = []
        for i in watchedmovie:
            if i.user_id == request.user.pk:
                my_watch_movie.append(i.movie_id)

        for i in watchedmovie:
            if i.movie_id == movie_pk and i.user_id == request.user.pk:
                delete_id = i.id
                watchmovie = get_object_or_404(WatchedMovie, pk=delete_id)
                watchmovie.delete()
                my_watch_movie.remove(movie_pk)
                break
        else:
            added_watched_movie = WatchedMovie(
                user_id=request.user.pk,
                movie_id=movie_pk
            )
            added_watched_movie.save()
            my_watch_movie.append(added_watched_movie.movie_id)
        return JsonResponse(my_watch_movie, safe=False)




# 리뷰 토크나이저
# 내가 작성한 리뷰를 리뷰 부분과 평점 부분으로 나누는 함수
def get_texts_scores(fname):
    # `fname` 파일은 영화평과 평점이 '&&' 으로 구분된 .txt 파일입니다.
    # with open(fname, encoding='utf-8') as f:
    docs = [doc.lower().replace('\n', '').split('&&') for doc in fname]
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



# 리뷰 작성 시 새 리뷰를 포함하여 해당 영화의 키워드를 리뉴얼하는 함수
def keyword_renewal(movie_pk):

    beta = 0.85    # PageRank의 decaying factor beta
    max_iter = 10

    top_keywords = []
    fnames = []
    reviews = Reviews.objects.all()
    modify_rev = []
    for review in reviews:
        if review.movie_id == movie_pk:
            modify_rev.append(review)
            review_txt = review.sentence + '&&' + str(review.score)
            fnames.append(review_txt)

    # for fname in fnames:
    texts, scores = get_texts_scores(fnames)

    wordrank_extractor = KRWordRank(min_count=5, max_length=10, verbose=False)

    keywords, rank, graph = wordrank_extractor.extract(texts, beta, max_iter)

    top_keywords.append(
        sorted(keywords.items(), key=lambda x: x[1], reverse=True)[:100])
    top_keywords = sum(top_keywords, [])

    get_common_keywords = CommonKeyword.objects.all()
    common_keywords = []
    for ck in get_common_keywords:
        common_keywords.append(ck.common_keyword)

    # # common_keywords를 제외한 필터링 된 키워드만을 추출하여 selected_top_keywords에 영화별로 담음
    selected_top_keywords = []
    for keywords in top_keywords:
        keywords = [keywords]
        # selected_keywords = []
        for word, r in keywords:
            if word in common_keywords:
                continue
            # selected_keywords.append((word, r))
            selected_top_keywords.append((word, r))

    keywords = Keyword.objects.all()
    keyword_list = []
    only_keyword_list = []
    for i in keywords:
        if i.movie_id == movie_pk:
            keyword_list.append(i)
            only_keyword_list.append(i.keyword)
    for k in range(len(selected_top_keywords)):
        res = get_from_list(selected_top_keywords, k)
        if res[0] not in only_keyword_list:
            added_keyword = Keyword(
                keyword=res[0],
                keyword_score=res[1],
                movie_id=movie_pk,
            )
            added_keyword.save()
            print('없는 키워드', res[0])
        else:
            for j in keyword_list:
                if j.keyword == res[0] and j.keyword_score != res[1]:
                    j.delete()
                    added_keyword = Keyword(
                        keyword=res[0],
                        keyword_score=res[1],
                        movie_id=movie_pk,
                    )
                    added_keyword.save()
                    print('값이 바뀐 키워드', res[0])



# 리뷰 작성 및 키워드 추출, 키워드 기반 매칭된 영화 반환 함수
@api_view(['POST'])
def create_review(request, movie_pk):
    wms = []
    watchedmovie = WatchedMovie.objects.all()
    for wm in watchedmovie:
        if wm.user_id == request.user.pk:
            wms.append(wm.movie_id)
    beta = 0.85    # PageRank의 decaying factor beta
    max_iter = 10

    top_keywords = []

    # 유저가 작성한 리뷰와 score를 && 기준으로 묶음
    fnames = [request.data['sentence'] + '&&' + str(request.data['score'])]
    # 새로 작성된 리뷰를 DB에 저장
    added_review = Reviews(
        sentence=request.data['sentence'],
        score=request.data['score'],
        movie_id=movie_pk,
        user_id=request.user.pk
    )
    added_review.save()

    keyword_renewal(movie_pk)

    # 텍스트와 스코어를 분리
    texts, scores = get_texts_scores(fnames)

    # 키워드 뽑아내기
    wordrank_extractor = KRWordRank(min_count=1, max_length=10, verbose=False)

    keywords, rank, graph = wordrank_extractor.extract(texts, beta, max_iter)

    # top_keywords = 내가 쓴 리뷰의 [(키워드, 스코어)]
    top_keywords.append(
        sorted(keywords.items(), key=lambda x: x[1], reverse=True)[:100])
    top_keywords = sum(top_keywords, [])

    get_common_keywords = CommonKeyword.objects.all()
    common_keywords = []
    for ck in get_common_keywords:
        common_keywords.append(ck.common_keyword)
    tmp = []
    for i in range(len(top_keywords)):
        if not top_keywords[i][0] in common_keywords:
            tmp.append(top_keywords[i][0])
    top_keywords = tmp

    movies_keywords = Keyword.objects.all()

    reco_movies = []
    if len(top_keywords) >= 3:
        for mRK in range(len(top_keywords)):
            reco = []
            for keywords in movies_keywords:
                if top_keywords[mRK] == keywords.keyword and keywords.movie_id not in wms:
                    reco.append(keywords)
            if reco:
                reco_movies.append(reco)
            if len(reco_movies) == 3:
                break
        reco_movies1 = sorted(reco_movies[0], key=lambda x: x.keyword_score, reverse=True)[:3]
        reco_movies2 = sorted(reco_movies[1], key=lambda x: x.keyword_score, reverse=True)[:3]
        reco_movies3 = sorted(reco_movies[2], key=lambda x: x.keyword_score, reverse=True)[:3]

        reco_movies1 = random.sample(reco_movies1, 1)
        reco_movies2 = random.sample(reco_movies2, 1)
        reco_movies3 = random.sample(reco_movies3, 1)
        reco_mov = []
        reco_mov.append(reco_movies1)
        reco_mov.append(reco_movies2)
        reco_mov.append(reco_movies3)
        reco_mov = sum(reco_mov, [])
        serializer = KeywordsSerializer(reco_mov, many=True)
        print(serializer.data)
        return Response(serializer.data)
    else:
        return JsonResponse(reco_movies, safe=False)
