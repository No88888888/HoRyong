# from . import get_movie
from django.urls import path
from . import views


app_name = "movies"
urlpatterns = [
    # path("", views.index, name="index"),
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('movies/<int:movie_pk>/reviews/', views.review_create, name='review_create'),
    path('reviews/<int:movie_pk>/', views.review_detail, name='review_detail'),
    # path('test/', get_movie.get_movie)
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