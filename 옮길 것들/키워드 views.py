from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

def get_texts_scores(fname):
    # 튜토리얼에서 이용하는 `fname` 파일은 영화평과 평점이 \t 으로 구분된 two column tsv 파일입니다.
    # 예시는 이 cell 의 output 을 참고하세요.
    with open(fname, encoding='utf-8') as f:
        docs = [doc.lower().replace('\n','').split('\t') for doc in f]
        docs = [doc for doc in docs if len(doc) == 2]

        if not docs:
            return [], []

        texts, scores = zip(*docs)
        return list(texts), list(scores)

# La La Land
fname = './data/134963.txt'
texts, scores = get_texts_scores(fname)

with open(fname, encoding="utf-8") as f:
    for _ in range(5):
        print(next(f).strip())

import sys
sys.path.append('../')
from krwordrank.word import KRWordRank
from krwordrank.hangle import normalize
import krwordrank
# print(krwordrank.__version__)

with open('./data/134963_norm.txt', 'w', encoding='utf-8') as f:
    for text, score in zip(texts, scores):
        text = normalize(text, english=True, number=True)
        f.write('%s\t%s\n' % (text, str(score)))

# La La Land
fname = './data/134963_norm.txt'
texts, scores = get_texts_scores(fname)

wordrank_extractor = KRWordRank(
    min_count = 5, # 단어의 최소 출현 빈도수 (그래프 생성 시)
    max_length = 10, # 단어의 최대 길이
    verbose = True
    )

beta = 0.85    # PageRank의 decaying factor beta
max_iter = 10

keywords, rank, graph = wordrank_extractor.extract(texts, beta, max_iter)

for word, r in sorted(keywords.items(), key=lambda x:x[1], reverse=True)[:30]:
    print('%8s:\t%.4f' % (word, r))