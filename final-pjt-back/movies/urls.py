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
