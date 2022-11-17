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
def get_texts_scores(fname):
    # `fname` 파일은 영화평과 평점이 '&&' 으로 구분된 .txt 파일입니다.
    with open(fname, encoding='utf-8') as f:
        docs = [doc.lower().replace('\n', '').split('&&') for doc in f]
        docs = [doc for doc in docs if len(doc) == 2]

        if not docs:
            return [], []

        texts, scores = zip(*docs)
        return list(texts), list(scores)

wordrank_extractor = KRWordRank(
    min_count=5,  # 단어의 최소 출현 빈도수 (그래프 생성 시)
    max_length=10,  # 단어의 최대 길이
    verbose=True
)

beta = 0.85    # PageRank의 decaying factor beta
max_iter = 10

top_keywords = []
fnames = ['./data/A Werewolf Boy.txt',
        './data/Aladdin.txt',
        './data/Avatar2022.txt',
        './data/Avengers Endgame.txt',
        './data/Avengers Infinity War.txt',
        './data/Begin Again.txt',
        './data/Contraband.txt',
        './data/Doctor Strange.txt',
        './data/Forrest Gump.txt',
        './data/Frozen.txt',
        './data/Harry Potter And The Chamber Of Secrets.txt',
        './data/Harry Potter And The Goblet Of Fire.txt',
        './data/Harry Potter And The Half-Blood Prince.txt',
        './data/Harry Potter And The Order Of The Phoenix.txt',
        './data/Harry Potter And The Prisoner Of Azkaban.txt',
        './data/Harry Potter And The Sorcerer\'s Stone.txt',
        './data/Home Alone.txt',
        './data/How To Train Your Dragon.txt',
        './data/In Time.txt',
        './data/Inception.txt',
        './data/Iron man.txt',
        './data/Jurassic World.txt',
        './data/La La Land.txt',
        './data/Les Miserables.txt',
        './data/Love Actually.txt',
        './data/Memento.txt',
        './data/Miracle in Cell No.7.txt',
        './data/Miracle.txt',
        './data/PARASITE.txt',
        './data/Race to Freedom Um Bok Dong.txt',
        './data/Secret.txt',
        './data/Snowpiercer.txt',
        './data/Spider-Man No Way Home.txt',
        './data/The Dark Knight Rises.txt',
        './data/The Gangster, The Cop, The Devil.txt',
        './data/The Greatest Showman.txt',
        './data/The Matrix.txt',
        './data/THE OUTLAWS.txt',
        './data/the roundup.txt',
        './data/The Sound Of Music.txt',
        './data/The Spiriting Away Of Sen And Chihiro.txt',
        './data/Titanic.txt',
        './data/topgun2.txt',
        './data/TRAIN TO BUSAN.txt',
        './data/Up.txt',
        './data/V For Vendetta.txt',
        './data/Vita Dolce.txt',
        './data/WALL-E.txt',
        './data/Zack Snyder\'s Justice League.txt',
        './data/Zootopia.txt',
        ]

# 각 영화 별 키워드 추출하여 top_keywords에 [[(키워드, 스코어)], [(키워드, 스코어)], [(키워드, 스코어)], ...] 형태로 저장
for fname in fnames:
    texts, scores = get_texts_scores(fname)

    wordrank_extractor = KRWordRank(min_count=5, max_length=10, verbose=False)

    keywords, rank, graph = wordrank_extractor.extract(texts, beta, max_iter)

    top_keywords.append(sorted(keywords.items(), key=lambda x: x[1], reverse=True)[:100])

# 가장 적은 키워드를 가진 영화의 키워드 수를 알아냄
minV = 99999999999
avg = 0
for i in range(50):
    avg += len(top_keywords[i])
    if len(top_keywords[i]) < minV:
        minV = len(top_keywords[i])
avg = avg//50
print('영화들 평균 키워드 개수:',avg)
print('최소 키워드 수:',minV)
# 모든 영화들에서 키워드의 숫자를 셈
keyword_counter = {}
for keywords in top_keywords:
    words, ranks = zip(*keywords)
    for word in words:
        keyword_counter[word] = keyword_counter.get(word, 0) + 1

# keyword_counter에서 영화의 개수만큼 나온 키워드를 common_keywords에 저장함(영화, 진짜 등등)
common_keywords = {word for word, count in keyword_counter.items() if count >= 10}
print('커먼 키워드:', common_keywords)
print('커먼 키워드 개수:',len(common_keywords))
# common_keywords를 제외한 진짜 키워드만을 추출하여 selected_top_keywords에 영화별로 담음
selected_top_keywords = []
for keywords in top_keywords:
    selected_keywords = []
    for word, r in keywords:
        if word in common_keywords:
            continue
        selected_keywords.append((word, r))
    selected_top_keywords.append(selected_keywords)

# 영화별 키워드와 스코어를 뽑아낼 함수
def get_from_list(l, i, default=('', 0)):
    if len(l) <= i:
        return default
    else:
        return l[i]

movie_id = [128246, 420817, 19995, 299534, 299536, 198277, 77866, 284052, 13, 19445, 672, 674, 767, 675, 673, 671, 771, 1191, 49530, 27205, 1726, 135397, 313369, 82695, 508, 77, 158445, 730823, 496243, 571783, 20342, 110415, 634649, 49026, 581528, 316029, 603, 479718, 619803, 15121, 129, 597, 361743, 396535, 14160, 752, 116196, 1681, 791373, 269149 ]

for i in range(50):
    # for k in range(minV - len(common_keywords)):
    # for k in range(len(selected_top_keywords[i]) - len(common_keywords)):
    cnt = 0
    # 각 영화 별 키워드 개수만큼 순회
    for k in range(len(selected_top_keywords[i])):
        cnt += 1
        res = get_from_list(selected_top_keywords[i], k)
        # 영화의 키워드가 커먼 키워드와 겹치면 통과
        if res[0] not in common_keywords:
            pass
            # print(cnt, movie_id[i], res[0], res[1])
    # print('#######################################')
