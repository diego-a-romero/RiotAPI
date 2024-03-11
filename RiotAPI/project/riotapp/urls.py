from django.urls import path
from . import views

urlpatterns = [
    path('', views.insert_games, name='insert_games'),
    path('show_games/', views.show_games, name='show_games'),
]