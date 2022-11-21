# db에서 리뷰 뽑아내기 위한 파일
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

@csrf_exempt
@api_view(['POST'])
def create_review(request):

    # 유저가 작성한 리뷰에서 키워드를 추출
    beta = 0.85    # PageRank의 decaying factor beta
    max_iter = 10

    top_keywords = []
    
    # fnames = './data/A Werewolf Boy (1).txt'
    fnames = request.data
    print(fnames)
    
    texts, scores = get_texts_scores(fnames)

    wordrank_extractor = KRWordRank(min_count=5, max_length=10, verbose=False)

    keywords, rank, graph = wordrank_extractor.extract(texts, beta, max_iter)

    top_keywords.append(sorted(keywords.items(), key=lambda x: x[1], reverse=True)[:100])
    top_keywords = sum(top_keywords,[])
    print(top_keywords)