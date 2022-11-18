# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status

# Create your views here.

import sys
sys.path.append('../')
import krwordrank
from krwordrank.hangle import normalize
from krwordrank.word import KRWordRank


# 리뷰 토크나이저
# def get_texts_scores(fname):
#     # `fname` 파일은 영화평과 평점이 '&&' 으로 구분된 .txt 파일입니다.
#     with open(fname, encoding='utf-8') as f:
#         docs = [doc.lower().replace('\n', '').split('&&') for doc in f]
#         docs = [doc for doc in docs if len(doc) == 2]
#         docs = [doc for doc in docs if len(doc) == 2]

#         if not docs:
#             return [], []

#         texts, scores = zip(*docs)
#         return list(texts), list(scores)



# wordrank_extractor = KRWordRank(
#     min_count=5,  # 단어의 최소 출현 빈도수 (그래프 생성 시)
#     max_length=10,  # 단어의 최대 길이
#     verbose=True
# )

# beta = 0.85    # PageRank의 decaying factor beta
# max_iter = 10

# top_keywords = []
# fnames = './data/A Werewolf Boy (1).txt'

# # fnames = ['./data/A Werewolf Boy (1).txt',
# #           './data/Aladdin (1).txt',
# #           './data/Avatar2022 (1).txt']

# # 각 영화 별 키워드 추출하여 top_keywords에 [[(키워드, 스코어)], [(키워드, 스코어)], [(키워드, 스코어)], ...] 형태로 저장
# # for fname in fnames:
# #     texts, scores = get_texts_scores(fname)

# #     wordrank_extractor = KRWordRank(min_count=5, max_length=10, verbose=False)

# #     keywords, rank, graph = wordrank_extractor.extract(texts, beta, max_iter)

# #     top_keywords.append(sorted(keywords.items(), key=lambda x: x[1], reverse=True)[:100])
# texts, scores = get_texts_scores(fnames)

# wordrank_extractor = KRWordRank(min_count=5, max_length=10, verbose=False)

# keywords, rank, graph = wordrank_extractor.extract(texts, beta, max_iter)

# top_keywords.append(sorted(keywords.items(), key=lambda x: x[1], reverse=True)[:100])
# top_keywords = sum(top_keywords,[])
# # print(len(top_keywords))
# # 가장 적은 키워드를 가진 영화의 키워드 수를 알아냄
# # minV = 99999999999
# # for i in range(3):
# #     if len(top_keywords[i]) < minV:
# #         minV = len(top_keywords[i])

# # 모든 영화들에서 키워드의 숫자를 셈
# keyword_counter = {}
# for keywords in top_keywords:
#     words, ranks = keywords
#     for word in words:
#         keyword_counter[word] = keyword_counter.get(word, 0) + 1
# # print('###############')
# # print(keyword_counter)
# # print('###############')
# # keyword_counter에서 영화의 개수만큼 나온 키워드를 common_keywords에 저장함(영화, 진짜 등등)
# # common_keywords = {word for word, count in keyword_counter.items() if count == 3}
# common_keywords = {word for word, count in keyword_counter.items()}
# common_keywords = {'송중기', '영화', '정말'}
# # common_keywords를 제외한 진짜 키워드만을 추출하여 selected_top_keywords에 영화별로 담음
# selected_top_keywords = []
# # print(top_keywords)
# # print('##########################')
# for keywords in top_keywords:
#     keywords = [keywords]
#     # selected_keywords = []
#     for word, r in keywords:
#         if word in common_keywords:
#             continue
#         # selected_keywords.append((word, r))
#     selected_top_keywords.append((word, r))
# # selected_keywords = []
# # for word, r in zip(top_keywords):
# #     if word in common_keywords:
# #         continue
# #     selected_keywords.append((word, r))
# # selected_top_keywords.append(selected_keywords)
# # print(selected_top_keywords)
# # 영화별 키워드와 스코어를 뽑아낼 함수
# def get_from_list(l, i, default=('', 0)):
#     if len(l) <= i:
#         return default
#     else:
#         return l[i]

# print(selected_top_keywords)
# # for i in range(3):
# # print(len(top_keywords), len(common_keywords))
# for k in range(len(selected_top_keywords)):
#     # print('for문:', selected_top_keywords)
#     res = get_from_list(selected_top_keywords, k)
#     # print(res)
#     print(res[0], res[1])
# # print('#######################################')



# 리뷰 토크나이저
# def get_texts_scores(fname):
#     # `fname` 파일은 영화평과 평점이 '&&' 으로 구분된 .txt 파일입니다.
#     with open(fname, encoding='utf-8') as f:
#         docs = [doc.lower().replace('\n', '').split('&&') for doc in f]
#         docs = [doc for doc in docs if len(doc) == 2]
#         docs = [doc for doc in docs if len(doc) == 2]

#         if not docs:
#             return [], []

#         texts, scores = zip(*docs)
#         return list(texts), list(scores)
    
# def get_from_list(l, i, default=('', 0)):
#     if len(l) <= i:
#         return default
#     else:
#         return l[i]
    
    
# def keyword_extractor():

#     beta = 0.85    # PageRank의 decaying factor beta
#     max_iter = 10

#     top_keywords = []
#     fnames = './data/A Werewolf Boy (1).txt'
    
#     texts, scores = get_texts_scores(fnames)

#     wordrank_extractor = KRWordRank(min_count=5, max_length=10, verbose=False)

#     keywords, rank, graph = wordrank_extractor.extract(texts, beta, max_iter)

#     top_keywords.append(sorted(keywords.items(), key=lambda x: x[1], reverse=True)[:100])
#     top_keywords = sum(top_keywords,[])
    
    
#     keyword_counter = {}
#     for keywords in top_keywords:
#         words, ranks = keywords
#         for word in words:
#             keyword_counter[word] = keyword_counter.get(word, 0) + 1

#     common_keywords = {word for word, count in keyword_counter.items()}
#     common_keywords = {'송중기', '영화', '정말'}
#     selected_top_keywords = []

#     for keywords in top_keywords:
#         keywords = [keywords]
#         # print(keywords)
#         for word, r in keywords:
#             if word in common_keywords:
#                 # print(common_keywords)
#                 continue
#             selected_top_keywords.append((word, r))
#     # print(selected_top_keywords)
#     for k in range(len(selected_top_keywords)):
#         res = get_from_list(selected_top_keywords, k)
#         print(res[0], res[1])
#     # print('#######################################3')
# keyword_extractor()