# from . import get_movie
# from . import views_2
from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    # path("", views.index, name="index"),
    path('', views.movie_list, name='movie_list'), # 영화 전체 리스트
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_pk>/create_review/', views.create_review, name='create_review'), # 영화 하나에 슬 리뷰
    path('<int:user_pk>/my_review/', views.my_review, name='my_review'),
    path('<int:movie_pk>/wish_list/', views.wish_list, name='wish_list'),
    path('<int:movie_pk>/watched_movie/', views.watched_movie, name='watched_movie'),
    # path('<int:movie_pk>/review_create/', views.review_create, name='review_create'),
    # path('test/', get_movie.get_movie),
    # path('test2/', views_2.keyword_extractor_many,),
]
    
    
        
#     path("create/", views.create, name="create"),
#     path("<int:pk>/", views.detail, name="detail"),
#     path("<int:pk>/delete/", views.delete, name="delete"),
#     path("<int:pk>/update/", views.update, name="update"),
#     path("<int:pk>/reviews/", views.reviews_create, name="reviews_create"),
#     path(
#         "<int:movie_pk>/reviews/<int:review_pk>/delete/",
#         views.reviews_delete,
#         name="reviews_delete",
#     ),
#     path("<int:movie_pk>/likes/", views.likes, name="likes"),
#     path('<int:hash_pk>/hashtag/', views.hashtag, name='hashtag'),
# ]