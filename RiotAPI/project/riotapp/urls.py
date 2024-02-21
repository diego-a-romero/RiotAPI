from django.urls import path
from . import views

urlpatterns = [
    path('', views.insert_games, name='insert_games'),
    path('success/', views.success, name='success_url'),
]