# Final PJT

# (주) 호룡정보통신
## 프로젝트 명: KEYMOO
사용자 작성 리뷰에서 키워드를 찾아내 매칭되는 영화를 추천해주는 웹사이트 서비스

# 1. 사전 설계
## 1) 핵심 알고리즘
> KR-WordRank : 한글 문장에서 단어 출현 빈도수와 문장 내 단어 혹은 형태소들 간의 호응도를
> 계산하여 키워드와 해당 키워드의 중요도(score)를 계산해내는 알고리즘 라이브러리
>
> 1. 위 라이브러리 이용하여 미리 영화 50개의 리뷰 DB를 크롤링해온 후
> 이를 이용하여 영화별 키워드를 추출하여 저장한다
>
> 2. 사용자가 영화에 리뷰를 작성 시 리뷰에서 키워드를 추출한 후 이와 맞는 영화를 찾아 추천하는 알고리즘 
## 2) ERD
> 아이디어를 기반으로 설계한 ERD
> 
> Movies : 영화 정보 Model
>
> User : 사용자 정보 Model
>
> Keywords : 영화들의 키워드 정보 Model
>
> Reviews : 영화들의 리뷰 정보 Model
>
> Wishlist : 사용자의 위시리스트 정보 Model
>
> WatchedMovie : 사용자의 본 영화 정보 Model
> 
![ERD](https://user-images.githubusercontent.com/109266776/203706466-8ba61c1b-cfe9-4504-b01b-bca435d3470c.png)

## 3) BE, FE
> 역할 분담
> 
> Backend : 김진호
> - model 작성
> - url 작성
> - views 함수 작성
> 
>
> Frontend : 권용재
> - 컴포넌트 작성
> - CSS 디자인
> 
## 4) MVP
> 1) 키워드 기반 영화 추천
> 2) 위시리스트 추가, 삭제 토글, 삭제
> 3) 워치드무비 추가, 삭제 토글
> 4) 리뷰 작성, 수정, 삭제
> 5) 로그인
> 6) 로그아웃
> 7) 회원가입

## 2. 구현
## **`DATA`**
1) model 작성
   
![image](https://user-images.githubusercontent.com/109266776/203711168-7f0f1b72-f84d-4947-a5bf-a3b33952694a.png)

- ERD 기반하여 model 작성
- wishlist, watchedmovie 등 user_id와 movie_id를 외래키로 갖는 중개테이블을 만들어준다
- 

1) 네이버 리뷰 데이터 크롤링
   
![네이버리뷰 크롤링py](https://user-images.githubusercontent.com/109266776/203709802-bb18ac0c-6a8b-4136-a71f-041da78a6340.png)

- 네이버 리뷰 크롤링해오는 프로그램을 이용하여 50개 영화에 대한 리뷰를 받아와 DB에 저장해준다
- .
- 

1) TMDB API
   
![tmbd에서_50영화_db받아오기](https://user-images.githubusercontent.com/109266776/203710319-70e4919e-7d48-49bd-9b89-fa62f3971af4.png)

- 네이버에서 리뷰를 받아온 영화 50개의 정보를 TMDB API를 이용하여 받아와 DB에 저장해준다
- .
- 


4) admin 계정 생성
- 기본 데이터로 넣을 리뷰들의 user_id 의존성 해결을 위해 admin 계정 생성


5) common_keyword와 keyword 추출
   
![view2_커먼키워드_추출_영화_키워드_추출_1](https://user-images.githubusercontent.com/109266776/203711909-df089b4f-c649-4520-aad3-b34c4a0ec7cd.png)

- 50개 영화의 리뷰를 KR-WordRank 라이브러리를 이용해 돌린다

![view2_커먼키워드추출_1(키워드, 키워드스코어)](https://user-images.githubusercontent.com/109266776/203712136-ea114d2b-1fa9-4d84-8901-772cb55b32cf.png)

- 리뷰의 텍스트와 평점 두 부분으로 나눠서 2중 배열 생성

![view2_커먼키워드추출_2(영화별 키워드 숫자 세기)](https://user-images.githubusercontent.com/109266776/203712141-1bd9a8e9-98bf-4ab3-b403-f916d5458407.png)

- 키워드들의 숫자를 셈

![view2_커먼키워드추출_3(중복출현_횟수기준_커먼키워드_추출)](https://user-images.githubusercontent.com/109266776/203712143-565f366a-a345-44a5-ad8d-a6c4eb3e58d8.png)

- 전체 영화들의 키워드들 중에서 `25개 이상` 영화에서 중복된 키워드를 common_keyword로 분류 후 DB에 저장

![view2_각 영화별 키워드 DB에 저장](https://user-images.githubusercontent.com/109266776/203712808-05f09ba6-ef4f-4e3d-b3cf-05afad23b6bc.png)

- 각 영화별 키워드 DB에 저장

  > ### DB
  - Movies
  - 
    ![image](https://user-images.githubusercontent.com/109266776/203767946-0812aaa1-6d5b-4836-b8a9-edbb81ee044f.png)

  - Reviews
  - 
    ![image](https://user-images.githubusercontent.com/109266776/203768280-9b1756ce-c52c-447d-8a81-593f46f752e9.png)

  - Keyword
  - 
    ![image](https://user-images.githubusercontent.com/109266776/203768504-c6ec779a-44d9-45ab-97ca-716bc770fb88.png)

  - CommonKeyword
  - 
    ![image](https://user-images.githubusercontent.com/109266776/203768657-6ecf5264-1e63-4542-9a65-f7a917c5a673.png)


**전체코드**
```python
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
        

```

## **`BACKEND`**
### 1) urls.py
```python
from django.urls import path
from . import get_movie
from . import views_2
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_pk>/create_review/', views.create_review, name='create_review'),
    path('my_review/<int:user_pk>/', views.my_review, name='my_review'),
    path('<int:movie_pk>/modify_myreview/<int:user_pk>/', views.modify_myreview, name='modify_myreview'),
    path('wish_list/<int:user_pk>/', views.wish_list, name='wish_list'),
    path('<int:movie_pk>/modify_wishlist/<int:user_pk>/', views.modify_wishlist, name='modify_wishlist'),
    path('<int:movie_pk>/watched_movie/', views.watched_movie, name='watched_movie'),
    path('get_watched_movie/', views.get_watched_movie, name='get_watched_movie'),
    path('<int:movie_pk>/movie_review/', views.movie_review, name='movie_review'),
    path('test/', get_movie.get_movie),
    path('test2/', views_2.keyword_extractor_many,),
]

```

### 2) views.py
```python
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

```

```plain text
로직 간단설명
1. 사용자는 watchmovie 즉 본 영화에만 리뷰 작성 가능
2. 리뷰 작성 후 제출 시 해당 리뷰에서 키워드를 추출
3. 키워드 3개 이상 추출 시(이하는 추천 불가) 키워드 스코어 순으로 해당 키워드를 가지고 있는 영화를 검색
4. 매칭되지 않는 키워드는 건너뛰고 상위 키워드 순으로 3개 키워드에 대한 영화들이 리스트에 담긴다
5. 각 키워드에 매칭된 영화들의 키워드 스코얻 각자 다름, 뎌기서 다시 키워드 스코어 별로 내림차순 정렬 후 상위 3개만 추출
6. 키워드마다 남은 3개씩의 영화들 중에서 랜덤으로 하나의 영화를 추출
7. 결과적으로 3개의 키워드, 각 키워드 당 랜덤으로 추출된 하나씩의 영화들 총 3개의 영화가 추천 됨
```

### 3) Serializer.py
```python
from rest_framework import serializers
from .models import Movies, Reviews, WishList, WatchedMovie, Keyword


class MoviesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movies
        fields = '__all__'


class ReviewsSerializer(serializers.ModelSerializer):
    class MyReviewSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movies
            fields = '__all__'

    class Meta:
        model = Reviews
        fields = '__all__'
        read_only_fields = ('movie', 'user')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['movie'] = self.MyReviewSerializer(instance.movie).data
        return response


class KeywordsSerializer(serializers.ModelSerializer):
    class MyKeywordSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movies
            fields = '__all__'

    class Meta:
        model = Keyword
        fields = '__all__'
        read_only_fields = ('movie',)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['movie'] = self.MyKeywordSerializer(instance.movie).data
        return response


class WishListSerializer(serializers.ModelSerializer):

    class MyWishListSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movies
            fields = '__all__'

    class Meta:
        model = WishList
        fields = '__all__'
        read_only_fields = ('movie', 'user')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['movie'] = self.MyWishListSerializer(instance.movie).data
        return response


class WatchedMovieSerializer(serializers.ModelSerializer):

    class MyWatchedMovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movies
            fields = '__all__'

    class Meta:
        model = WatchedMovie
        fields = '__all__'
        read_only_fields = ('movie', 'user')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['movie'] = self.MyWatchedMovieSerializer(instance.movie).data
        return response

```

- 리뷰, 키워드, 워치드 무비 등의 정보를 반환해주기 위한 serializer들
- 각 정보에 무비 정보를 함께 담기 위해 내부에 My~serializer를 override

### 4) settings.py
- 로그인, 로그아웃, 회원가입, cors, permissions 등을 위한 패키지 설치 및 설정
```python
INSTALLED_APPS = [
    'accounts',
    'movies',
    'rest_framework',
# CORS policy
    "corsheaders",

    # Auth
    'rest_framework.authtoken',
    'dj_rest_auth',

    # registration
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',

    # OpenAPI 3.0
    # 'drf_spectacular',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

SITE_ID = 1

REST_FRAMEWORK = {
    # Authentication
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],

    # permission
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny',
    ],

    # spectacular Settings
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Your Project API',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

### `FRONTEND`

### 1) App.vue
```html
<template>
  <body>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.9.1/font/bootstrap-icons.css">
    <div id="app">
      <nav id="navbar" class="navbar navbar-expand-lg navbar-light navbar-fixed-top">
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo03" aria-controls="navbarTogglerDemo03" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <!-- 아이콘으로 링크 보내기 -->
        <router-link id="Icon" class="navbar-brand" :to="{ name: 'MovieView' }">HoRyong</router-link>
          <div class="collapse navbar-collapse d-flex justify-content-between" id="navbarTogglerDemo03">
            
            <div class="form-inline my-2 my-lg-0">
            </div>

            <ul class="navbar-nav mr-auto mt-2 mt-lg-0 d-flex justify-content-end">
              <li id="liTag" class="nav-item active">
                <router-link class="nav-item " :to="{ name: 'MovieView' }">Movies</router-link>
              </li>
              <li id="liTag" class="nav-item">
                <router-link class="nav-item" :to="{ name: 'ProfileView' }" v-show="isLogedIn">Profiles</router-link>
                <router-link class="nav-item" :to="{ name: 'SignUpView' }" v-if="!isLogedIn">Sign Up</router-link> 
              </li>
              <li id="liTag" class="nav-item">
                <a class="nav-item" v-show="isLogedIn" @click.prevent="logOut">Logout</a>
                <router-link class="nav-item" :to="{ name: 'LoginView' }" v-if="!isLogedIn">Login</router-link>
              </li>
            </ul>
          </div>
      </nav>
      <router-view/>

    </div>
  </body>
</template>
<script>


export default {
  name : "App",
  computed: {
    isLogedIn() {
      return this.$store.state.username
    }
  },
  methods: {
    logOut() {
      this.$store.dispatch('logout')
    }
  }
}
</script>

<style scopd>
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.9.1/font/bootstrap-icons.css");
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #ffffff;
}

nav {
  padding: 30px;
  z-index: 1;
}

#navbar {
  position: absolute;
  /* overflow: hidden; */
  background-color: none;
  opacity: 1;
}

#Icon {
  display: block;
  color: #f2f2f2;
  text-align: center;
  padding: 10px;
  text-decoration: none;
  font-weight: bold;
}

#liTag > a {
  display: block;
  color: #f2f2f2;
  text-align: center;
  padding: 10px;
  text-decoration: none;
  font-weight: bold;
}

#liTag > a.router-link-exact-active {
  color: #42b983;
}
#liTag > a.exact-active {
  color: #42b983;
}

.navbar-nav {
  width: 30% !important;

}

/* .content {
  padding: 16px;
}

.sticky {
  position: fixed;
  top: 0;
  width: 100%;
}
.sticky + .content {
  padding-top: 60px;
} */

body {
	background: linear-gradient(-45deg, #ffffff, #000000, #ffffff, #000000);
	background-size: 400% 400%;
	animation: gradient 10s ease infinite;
	height: 100vh;
}

/* @keyframes gradient {
	0% {
		background-position: 0% 50%;
	}
	50% {
		background-position: 100% 50%;
	}
	100% {
		background-position: 0% 50%;
	}
} */

</style>
```

### 2) MovieView.vue

```html
<template>
  <div>
    <h1>Movie Page</h1>
    <hr>
    <MovieLists @to-movie-view="openModal"/>


    <!-- 컴포넌트 MyModal -->
    <ReviewModal @close="closeModal" v-if="modal">
      <!-- default 슬롯 콘텐츠 -->
      <p>영화의 리뷰를 입력해서 다른 영화를 추천 받아 보세요!</p>
      <div>
        <img :src="imgUrl" alt="">
      </div>
      <div><input v-model.trim="message"></div>
      <!-- /default -->
      <div>
        <star-rating v-model="score" :increment="0.5" :animate=true :glow=10></star-rating>
      </div>
      <!-- footer 슬롯 콘텐츠 -->
      <template slot="footer">
        <button @click="doSend">제출</button>
      </template>
      <!-- /footer -->
    </ReviewModal>
  </div>
</template>

<script>
import StarRating from 'vue-star-rating'
import MovieLists from '@/components/MovieLists'
import ReviewModal from '@/components/ReviewModal'
// import router from '@/router'

export default {
    name : 'MovieView',
    components: {
        MovieLists,
        ReviewModal,
        StarRating,
    },
    data() {
      return {
        modal: false,
        message: '',
        movie : null,
        imgUrl: '',
        sendMessage: '',
        score: 0,
      }
    },
    methods: {
      openModal(submitData) {
        console.log(submitData)
        this.modal = submitData.modal
        this.movie = submitData.movie
        console.log(this.movie)
        this.imgUrl = 'https://image.tmdb.org/t/p/w220_and_h330_face/' + this.movie.poster_path
        
      },
      closeModal() {
        this.modal = false
        this.message = ''
      },
      getRecommendation() {
      
      },
      doSend() {
        if (this.message.length > 0) {
          alert(this.message)
          this.sendMessage = this.message
          this.message = ''

          const payload = {
          pk: this.movie.id,
          sentence: this.sendMessage,
          score: this.score*2,
          }
          
          console.log("제출할 때 넘겨 주는 데이터", payload)
          this.$store.dispatch('submitReview', payload)
          this.closeModal()
        } else {
          alert('메시지를 입력해주세요.')
        }

        // router.push({ name: 'RecommendView' })
      },
      // computed: {
      //   imgUrl() {
      //     const url = 'https://image.tmdb.org/t/p/w220_and_h330_face/' + this.movie.poster_path
      //     return url
      //   }
      // }
    }    
}
</script>

<style scoped>
h1 {
    font-size: 60px;
    color: linear-gradient(to right top, #000000, #ffffff);
    animation: gradient 10s ease infinite;
}
</style>
```
### 3) RecommendView
```html
<template>
<!-- <div> -->
  <div id="app" :style="{ backgroundImage: 'linear-gradient(to bottom, rgba(0, 0, 0, 0.6) 10%, rgba(0, 0, 0, 0.7) 25%, rgba(0, 0, 0, 0.8) 50%, rgba(0, 0, 0, 0.9) 75%, rgba(0, 0, 0, 1) 100%), url(' + backdroppath + ')', backgroundSize: 'cover' }">
    <h1>Recommend Page</h1>
    <div>
      <h2>{{ username }} 님이 작성하신 리뷰의 키워드는</h2>
      <h2>"{{ firstMovie.keyword }}"입니다.</h2>
      <h2>해당 키워드로 추천 드릴 영화는</h2>
      <h3>"{{ firstMovie.movie.title }}" 입니다.</h3>
      <img :src="firstMovieImg" alt="" />
    <div>
        <div @click="wishListToggle">
          <i class="bi bi-bookmark-star" v-if="!is_wish_movie"></i>
          <i class="bi bi-bookmark-star-fill" v-if="is_wish_movie"></i>
        </div>
    </div>
      <h2>{{ username }} 님의 다른 키워드</h2>
      <div>
        <span>
          두번 째 키워드:
          <div @click="changeToSecond">{{ secondMovie.keyword }}</div>
        </span>
      </div>
      <div>
        <span>
          세번 째 키워드:
          <div @click="changeToThird">{{ thirdMovie.keyword }}</div>
        </span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: "RecommendView",
  data() {
    return {
      movie: this.$store.state.recommendMovie,
      user_id : null,
      is_wishlist : null,
    };
  },
  
  computed: {
    is_wish_movie() {
      const wishlists = this.$store.state.wishlist.data
      if (wishlists) {
        console.log(wishlists)
        for (let wish of wishlists) {
          if (wish.movie.id === this.firstMovie.movie.id && wish.user === this.user_id) {
            return true
          } 
        }
        return false
      }
      return false
    },
    backdroppath() {
      return (
        'https://image.tmdb.org/t/p/original' +
        this.$store.state.recommendMovie[0].movie.backdrop_path
      );
    },
    firstMovie() {
      return this.$store.state.recommendMovie[0];
    },
    username() {
      return this.$store.state.username;
    },
    firstMovieImg() {
      return (
        "https://image.tmdb.org/t/p/w220_and_h330_face/" +
        this.$store.state.recommendMovie[0].movie.poster_path
      );
    },
    
    secondMovie() {
      return this.$store.state.recommendMovie[1];
    },
    thirdMovie() {
      return this.$store.state.recommendMovie[2];
    },
  },
  created() {
    this.getUserPk()
  },
  methods: {
    getUserPk() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
            this.user_id = res.data.pk
            return {'user_id': res.data.pk}
      })
    },
    changeToSecond() {
      this.$store.dispatch("switchWithSecond");
      this.$router.push({ name: "RecommendView" });
      this.$router.go();
    },
    changeToThird() {
      this.$store.dispatch("switchWithThird");
      this.$router.push({ name: "RecommendView" });
      this.$router.go();
    },
    wishListToggle() {
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.firstMovie.movie.id}/modify_wishlist/${this.user_id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
          this.$store.dispatch('saveWishList', res)
        })
      
    }
  }
};
</script>

<style>
</style>
```

### 4) DetailView
```html
<template>
  <div id="app" class="background" :style="{ backgroundImage: 'linear-gradient(to bottom, rgba(0, 0, 0, 0.6) 10%, rgba(0, 0, 0, 0.7) 25%, rgba(0, 0, 0, 0.8) 50%, rgba(0, 0, 0, 0.9) 75%, rgba(0, 0, 0, 1) 100%), url(' + backdroppath + ')', backgroundSize: 'cover' }">
    
    <h1 class="mb-5">Detail</h1>
    <div class="dummy-box">
    </div>
    <div class="container my-5">
      <div class="row">
        <div class=" single_column col-4">
          <!-- <section id="original_header" class="main"> -->
            <!-- 여기가 포스터 -->
          <div class="poster">
            <img :src="imgUrl" alt="#" class="image-sized">
          </div>
          <!-- 나우 워치로 보낼 디브 -->
          <div class="ott_offer">
            <div class="button">
              <div class="text">
                <span>
                  <h4>Now Streaming</h4>
                  <a class="no_click" :href="renderwatchUrl" title="#" target="_blank">Watch Now</a>
                </span>
              </div>
            </div>
          </div>
        </div>
          <!-- 여기가 제목 평점 및 내용 -->
        <div class="movie-info col-8">
          <div class="movie-title">
            <h2>{{ movie.title }}  ({{year}})</h2>
          </div>
          
          <div class="dummy-box">
          </div>
          <div class="movie-rate">
            <p>평점: {{ movie.vote_average }}</p>
            <p>장르: {{ genres }}</p>
          </div>
          
          <div class="movie-overview">
            <h5>개요</h5>
            <p>{{ movie.overview }}</p>
          </div>
        </div>
      </div>
  </div>
  <div class="container">
    <div class="text-left">
      <DetailReviews
        class="review-items"
        v-for="(review,index) in reviews_sliced"
        :key="review.id"
        :review="review"
        :index="index"
      />
    </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios'
import DetailReviews from '@/components/DetailReviews'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailView',
  components:{
    DetailReviews,
  },
  data() {
    return {
      movie: null,
      watchUrl: null,
      tmdbAPIKey: 'eb54cff7c77bbeb1441eaa6be7f211a1',
      imgUrl: '',
      reviews: null,
      backdrop : null,
      limit : 10,
      reviews_sliced : null,
    }
  },
  computed: {
    renderwatchUrl() {
      return this.watchUrl
    },
    year() {
      const cut = this.movie.release_date.substr(0, 4);
      return cut
    },
    genres() {
      const genreitems = this.movie.genres
      console.log(genreitems)
      let genrename = ''
      genreitems.forEach((genre) => {
        genrename += genre.name + ', '
      })
      let result = genrename.slice(0, -2);
      return result
    },
    backdroppath() {
      return this.backdrop
    }
  },
  created() {
    this.getMovieDetail()
    this.getMovieReviews()
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.id}/`
      })
        .then((res) => {
          this.movie = res.data
          this.imgUrl = 'https://image.tmdb.org/t/p/w220_and_h330_face/' + this.movie.poster_path
          this.backdrop = 'https://image.tmdb.org/t/p/original' + this.movie.backdrop_path
          document.documentElement.style.setProperty('--backdrop', 'url("' + this.backdrop + '")')
          console.log('스타일',document.documentElement.style)
          return res.data
        })
        .then((res) => {
          console.log(2,res)
          this.getWatchUrl()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getMovieReviews(){
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.id}/movie_review/`
      })
      .then((res) => {
        this.reviews = res.data
        console.log('this.reviews', this.reviews)
      })
      .then(() => {
        this.reviews_sliced = this.limit ? this.reviews.slice(0,this.limit) : this.reviews
        console.log('reviews_sliced', this.reviews_sliced)
      })
    },
    getWatchUrl() {
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${this.movie.movie_id}/watch/providers?api_key=${this.tmdbAPIKey}`
      })
        .then((res) => {
          console.log(res.data.results.KR.link)
          this.watchUrl = res.data.results.KR.link
          return this.watchUrl
        })
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap');
#app {
  font-family: 'Noto Sans KR', sans-serif, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: white;
  height: 100%;
}
/* .background{
  height: 100%;
}
.background::after{
  display: block;
  content: '';
  width: 100%;
  height: 100%;
  background-size: cover;
  background: linear-gradient(
    to bottom,
    rgb(251, 251, 251) 10%,
    rgba(206, 206, 206, 0.7) 25%,
    rgba(120, 120, 120, 0.8) 50%,
    rgba(80, 80, 80, 0.9) 75%,
    rgba(0, 0, 0, 1) 100%
  ), var(--backdrop);
  z-index: -1;
} */

/* .background {
  height: 100%;
  }
.background::after {
  height: 100%;
  width: 100%;
  content: "";
  background-image: linear-gradient(
            to bottom,
            rgba(255, 255, 255, 0) 70%,
            rgba(255, 255, 255, 0.5) 80%,
            rgba(255, 255, 255, 0.75) 90%,
            rgb(255, 255, 255) 100%
          ), var(--backdrop);

  overflow: hidden;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  opacity: 30%;

  top: 0;
  left: 0;
  z-index: -1;
  position: relative;
} */
.dummy-box{
  height:50px
}
.poster > img {
  max-width: 100%;
  height: auto;
}
.movie-title h2{
  position:relative;
  text-align:left;
}
.movie-rate p{
  position:relative;
  text-align:left;
}
.movie-overview p{
  position:relative;
  text-align:left;
}
.movie-overview h5{
  position:relative;
  text-align:left;
  font-weight: bold;
}
.text-left {
  text-align: left;
}


</style>
```
`이하 컴포넌트 생략`

### 5) store index.js
```javascript
import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    movies: [],
    token: null,
    recommendMovie: null,
    username: null,
    watchedMovie: null,
    wishlist: [],
    myReviewList:[],
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    // 회원가입 && 로그인
    SAVE_TOKEN(state, token) {
      state.token = token
    },
    RECOMMEND_MOVIE(state, recommendation) {
      state.recommendMovie = recommendation
    },
    WISHLIST_MOVIE(state, mywishlist) {
      state.wishlist = mywishlist
    },
    SWITCH_SECOND(state) {
      const temp = state.recommendMovie[0]
      state.recommendMovie[0] = state.recommendMovie[1]
      state.recommendMovie[1] = temp
    },
    SWITCH_THIRD(state) {
      const temp = state.recommendMovie[0]
      state.recommendMovie[0] = state.recommendMovie[2]
      state.recommendMovie[2] = temp     
    },
    SAVE_WATCHED(state, data) {
      state.watchedMovie = data
    },
    DELETE_ALL(state) {
      state.movies = [],
      state.token = null,
      state.recommendMovie = null,
      state.username = null,
      state.watchedMovie = null
    },
    GET_MY_REVIEWS(state,data) {
      state.myReviewList = data
    }
  },
  actions: {
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/`,
      })
        .then((res) => {
          context.commit('GET_MOVIES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        }
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
          context.state.username = payload.username
        })
        .then(() => {
          router.push({ name: 'MovieView' })
        })
    },
    login(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        },
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
          context.state.username = payload.username
        })
        .then(() => {
          axios({
            method: 'get',
            url: `${API_URL}/movies/get_watched_movie/`,
            headers: {
              Authorization: `Token ${context.state.token}`
            }
          })
          .then((res) => {
            console.log(res.data)
            context.commit('SAVE_WATCHED', res.data)
          })
          .then(() => {
            router.push({ name: 'MovieView' })
          })
        })
    },
    logout(context) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
          context.commit('DELETE_ALL')
          router.go()
        })
    },
    submitReview(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/movies/${payload.pk}/create_review/`,
        data: {
          movie_pk: payload.pk,
          sentence: payload.sentence,
          score: payload.score,
        },
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) =>{
          console.log("리뷰 제출 데이터", res.data)
          context.commit('RECOMMEND_MOVIE', res.data)
        })
        .then(() => {
          router.push({ name: 'RecommendView' })
        })
    },
    // submitWishList(context, payload) {
    //   axios({
    //     method: 'post',
    //     url: `${API_URL}/movies/${payload.movie_id}/modify_wishlist/${payload.pk}/`,
    //     data: {
    //       movie_pk: payload.movie_id,
    //     },
    //     headers: {
    //       Authorization: `Token ${context.state.token}`
    //     }
    //   })
    //     .then((res) =>{
    //       console.log("위시리스트 제출 데이터", res.data)
    //       context.commit('WISHLIST_MOVIE', res.data) 
    //   })
    // },
    getMyReviews(context) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          const user_pk = res.data.pk
          this.username = res.data.username
          axios({
            method: 'get',
            url: `${API_URL}/movies/my_review/${user_pk}/`,
            headers: {
              Authorization: `Token ${context.state.token}`
            }
          })
          .then((res) => {
            console.log('GET_MY_REVIEWS',res.data)
            context.commit('GET_MY_REVIEWS',res.data)
          })
        })

    },
    switchWithSecond(context) {
      context.commit('SWITCH_SECOND')
    },
    switchWithThird(context) {
      context.commit('SWITCH_THIRD')
    },
    saveWatchedMovie(context, data) {
      context.commit('SAVE_WATCHED', data)
    },
    saveWishList(context, data) {
      context.commit('WISHLIST_MOVIE', data)
    }
  },
  modules: {
  }
})

```

### 6) router index.js
```javascript
import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '@/views/MovieView'
import ProfileView from '@/views/ProfileView'
import MyReview from '@/components/MyReview'
import WishList from '@/components/WishList'
import DetailView from '@/views/DetailView'
import SignUpView from '@/views/SignUpView'
import LoginView from '@/views/LoginView'
import RecommendView from '@/views/RecommendView'
import store from '@/store/index.js'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MovieView',
    component: MovieView
  },
  {
    path: '/profile',
    name: 'ProfileView',
    component: ProfileView,
    children : [
      {
        path: '/myreview',
        name: 'MyReview',
        component: MyReview,
        beforeEnter(to, from, next) {
          console.log('비포 엔터',store.state.username)
          if(!store.state.username) {
            alert('로그인 후 접근할 수 있는 페이지 입니다.')
            next({ name: 'LoginView'})
          } else {
            next()
          }
        }
      },
      {
        path: '/wishlist',
        name: 'WishList',
        component: WishList,
        beforeEnter(to, from, next) {
          console.log('비포 엔터',store.state.username)
          if(!store.state.username) {
            alert('로그인 후 접근할 수 있는 페이지 입니다.')
            next({ name: 'LoginView'})
          } else {
            next()
          }
        }
      }
    ],
    beforeEnter(to, from, next) {
      console.log('비포 엔터',store.state.username)
      if(!store.state.username) {
        alert('로그인 후 접근할 수 있는 페이지 입니다.')
        next({ name: 'LoginView'})
      } else {
        next()
      }
    }
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView,
    beforeEnter(to, from, next) {
      if(store.state.username) {
        alert('로그아웃 후에 회원가입을 시도하세요.')
        next({ name: 'MovieView'})
      } else {
        next()
      }
    }
  },
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView,
    beforeEnter(to, from, next) {
      if(store.state.username) {
        alert('이미 로그인이 되어있습니다.')
        next({ name: 'MovieView'})
      } else {
        next()
      }
    }
  },  
  {
    path: '/recommend',
    name: 'RecommendView',
    component: RecommendView,
  },
  {
    path: '/:id',
    name: 'DetailView',
    component: DetailView,
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// router.beforeEach((to, from, next) => {
//   // 접근 가능 여부(로그인 상태면 true, 비로그인 상태면 false)
//   const authenticationState = store?.state?.token? true : false

//   console.log('to', to)
//   // 이동할 사이트가 인증을 필요로 하는 사이트인 경우
//   const authentication = ['SignUpView', 'LoginView'].includes(to.name)? false: true

//   console.log('authenticationState', authenticationState)
//   console.log('authentication', authentication)

//   console.log('From To',from, to)
//   // 비로그인 상태 && 이동하려는(이동할) 사이트가 로그인 해야만 하는 사이트인 경우 
//   if (!authenticationState && authentication) {
//     next({name: 'LoginView'})
//   }
//   else {
//     next()
//   }
// })

export default router
```
### 7) 컴포넌트 트리
![image](https://user-images.githubusercontent.com/109266776/203788056-7c41c326-3349-4ca0-87df-9078d68f652d.png)


## __USER FLOW__
1. 회원가입
2. 사용자 로그인
3. 무비 리스트 화면 이동
4. 워치드선택 시 ( 해당 영화를 봤다 ) 리뷰 작성 토글 활성화 및 리뷰 작성 가능
5. 리뷰 작성, 평점 주기
6. 해당 리뷰를 기반으로 다른 영화 추천 받기
7. 추천 받은 영화를 위시리스트에 추가 가능
8. 사용자 프로필 화면 이동
9.  마이 리뷰 이동 시 사용자가 작성한 모든 리뷰 조회 가능, 수정, 삭제 가능
10. 위시리스트 페이지 이동
11. 사용자 위시리스트 조회 가능, 수정, 삭제 가능

12. 무비 리스트 화면에서 각 영화 디테일페이지 이동
13. 영화 세부정보 및 해당 영화의 사용자 리뷰들 조회 가능, TMDB 사이트로 이동하는 링크 사용 가능
14. 로그아웃

## `WEB`
![image](https://user-images.githubusercontent.com/109266776/203788639-97adf50f-0d36-4c61-be6f-8dbcbe11cf12.png)

![image](https://user-images.githubusercontent.com/109266776/203788768-b5bbc580-a1e9-4814-b738-e1d78d41d941.png)

- 하단 `watched` 클릭 시 빨간 테두리 효과

![image](https://user-images.githubusercontent.com/109266776/203788964-8be526c5-f79d-45a1-a070-5da796d08a6f.png)

- 이미 리뷰 작성한 영화에서 리뷰 작성 클릭 시 alert 및 마이 리뷰 페이지로 리다이렉트

![image](https://user-images.githubusercontent.com/109266776/203789205-4386e2e8-0862-4c6e-96b2-ec1c78d2ff61.png)

- 리뷰 작성

![image](https://user-images.githubusercontent.com/109266776/203789326-4e22b562-9c46-4c5a-9b69-a235653f0057.png)

- 키워드 기반 추천 영화 페이지, 위시리스트 추가 가능

![image](https://user-images.githubusercontent.com/109266776/203789467-17ff18b5-9b03-4497-ac46-d07461fb29e7.png)

- 내리뷰 화면

![image](https://user-images.githubusercontent.com/109266776/203789672-cee3ffed-bcb2-4081-b8dc-ef7bb517f02a.png)

- 위시리스트 화면
- 이미지 클릭 시 상단에 해당 영화 세부 정보 실시간 팝업

![image](https://user-images.githubusercontent.com/109266776/203789876-2ed6d3c5-3085-4d9e-a631-7246a7132807.png)

- 디테일화면
- 영화 디테일 정보 및 사용자들의 리뷰 조회 가능


# 파이널 프로젝트를 마치며

## 아쉬웠던 점
김진호:
1. 프로젝트 기간이 너무 짧았다
2. 추천 알고리즘을 가져와서 분석하고 적용시키는데 너무 많은 시간을 써 실제 웹사이트 구현하는 시간이 부족했다
3. 기본 데이터를 넣기 위해 json 데이터 파일을 수동으로 작성했다. 하지말아야 할 행동 중 하나였는데...
4. 프로젝트가 처음이다보니 장님이 코끼리 더듬듯이 진행되었다. 앞의 내용들이 뒤에 문제를 일으키거나 더 필요해서 수정하게 되는 경우가 발생하였다.(model 등)
5. 시간이 부족하여 CSS가 약했다

권용재:
생각보다 시간이 많이 촉박했다. 약 12일정도의 시간을 가졌지만 메인 기능을 구상하는데 시간을 많이 소비한 것 같다. 아이디어 도출에도 시간을 많이 썼지만, 선택한 아이디어가 시간 내에 구현이 가능한 건지 가늠이 가질 않아서 불안한 상태로 시작을 했다. 계속 프로젝트를 진행하면서 이미 어느정도 자리를 잡았다고 생각했는데 하나가 막히면 아예 프로젝트를 처음부터 해야하는 상황도 마주쳤었고 계속해서 불안한 상태로 진행하는 것이 부담스러웠다.
또한 초반에 남들은 기본 틀을 만들면서 시작을 했는데 우리는 알고리즘이 작동하지 않는다면 의미가 없는 프로젝트였기 때문에 알고리즘에 4일을 투자하면서 많은 시간을 쏟아 냈다. 이로 인해서 시간 압박을 계속 느끼면서 프로젝트를 진행 하였고 부담감에 초반부터 많이 무리를 한 탓에 후반에 살짝 기세가 꺾였다.
10000개 이상의 데이터를 가져와서 분석 후 우리의 알고리즘에 적용한다면 좋은 결과 값이 나올 줄 알았지만 생각보다 기대에 못 미쳐서 아쉬웠다. 알고리즘 자체가 정말 좋게 짜여져 있었기 때문에 훨씬 많은 데이터들을 가지고 한다면 엄청 좋은 결과를 낼 수 있었을 텐데 그게 조금 아쉽다.

## 느낀 점
김진호:
1. 구현보다 사전 설계단계가 더 중요하다는 사실을 느꼈다. model 작성이라거나 알고리즘 실현 가능성 등 두들겨보지 않고 돌다리를 건넜을 시 발생 할 수 있는 문제들을 미리 확인하는 작업이 중요했다.
2. 백과 프론트 간의 정보 전달이 중요했다. 프론트에서 백으로 요청 시 반환해 줄 데이터를 정리하기 위해 로직을 복잡하게 정리 하였는데 프론트에서 넘어오는 data를 이용하여 쉽게 조회, 전달 해 줄 수 있었다.
3. 의견과 성향이 맞지 않는 팀원과의 팀프로젝트 - 우리 팀은 준수하였으나 타 팀들을 봤을 때 성향이 맞이 않아 약간의 갈등을 빚는 팀들을 보았다. 이런 경우에 어덯게 의견을 조율해 나갈 것인지가 중요할 것이라고 느꼈다
   
권용재:
교수님께서 조금 힘드시지 않겠냐고 한 3번 정도 하셨는데 매번 그 벽을 넘어서 해냈단 것이 뿌듯하다. 말씀 하실 때 마다 하던 것들을 중지해야 하나 생각이 들 정도로 큰 벽에 많이 부딪혔지만, 진호와 계속해서 하나 씩 해결해 나가면서 많이 성장함을 느꼈다. 어려운 주제를 선정했음에도 끝까지 포기하지 않고 나보다 훨씬 더 많은 노력으로 같이 프로젝트를 진행해준 진호에게 정말 많은 감사함을 느낀다. 팀원의 노력에 진짜 보답하기 위해서 마지막까지 쥐어 짜내서 좋은 결과가 있었으면 좋겠다. 진호랑 같은 팀을 하지 않았더라면 아마 정말 성공하지 못했을 프로젝트였다고 생각한다.