from django.urls import path
from . import views

urlpatterns = [
    path('insert_games/', views.insert_games, name='insert_games'),
]