from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    # path('<int:user_pk>/my_review', views.my_review, name='my_review'),
    path('<int:user_pk>/wishlist/', views.wish_list, name='wish_list'),
    # path('delete/', views.delete, name='delete'),
    # path('update/', views.update, name='update'),
    # path('password/', views.change_password, name='change_password'),
    
]