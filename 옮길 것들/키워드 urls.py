from django.urls import path
from . import views

app_name = 'extractor'
urlpatterns = [
    path('', views.get_texts_scores),
]