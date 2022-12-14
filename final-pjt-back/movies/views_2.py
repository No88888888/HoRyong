# Create your views here.
from .models import CommonKeyword, Keyword
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

# 영화별 키워드와 스코어를 뽑아낼 함수
def get_from_list(l, i, default=('', 0)):
    if len(l) <= i:
        return default
    else:
        return l[i]

def keyword_extractor_many(request):

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
    # minV = 99999999999
    # avg = 0
    # for i in range(50):
    #     avg += len(top_keywords[i])
    #     if len(top_keywords[i]) < minV:
    #         minV = len(top_keywords[i])
    # avg = avg//50
    # 모든 영화들에서 키워드의 숫자를 셈
    keyword_counter = {}
    for keywords in top_keywords:
        words, ranks = zip(*keywords)
        for word in words:
            keyword_counter[word] = keyword_counter.get(word, 0) + 1

    # keyword_counter에서 영화의 개수만큼 나온 키워드를 common_keywords에 저장함(영화, 진짜 등등)
    common_keywords = [word for word, count in keyword_counter.items() if count >= 25]
    
    for j in common_keywords:
        
        add_common_keywords = CommonKeyword(
            common_keyword = j,
        )
        add_common_keywords.save()
    
    # 커먼키워드 DB에서 커먼키워드 가져오기
    # get_common_keywords = CommonKeyword.objects.all()
    # common_keywords = []
    # for ck in get_common_keywords:
    #     common_keywords.append(ck.common_keyword)

    # common_keywords를 제외한 진짜 키워드만을 추출하여 selected_top_keywords에 영화별로 담음
    selected_top_keywords = []
    for keywords in top_keywords:
        selected_keywords = []
        for word, r in keywords:
            if word in common_keywords:
                continue
            selected_keywords.append((word, r))
        selected_top_keywords.append(selected_keywords)



    for i in range(50):
        cnt = 0
        # 각 영화 별 키워드 개수만큼 순회
        for k in range(len(selected_top_keywords[i])):
            cnt += 1
            res = get_from_list(selected_top_keywords[i], k)
            # 영화의 키워드가 커먼 키워드와 겹치면 통과
            if res[0] not in common_keywords:
                added_keyword = Keyword(
                    movie_id = i+1,
                    keyword = res[0],
                    keyword_score = res[1],
                )
                added_keyword.save()
        
