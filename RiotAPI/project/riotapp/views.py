from django.shortcuts import render, redirect
from django.http import HttpResponse
from .riotdata import search_games_from_riot_api
from .models import Game


def show_games(request):
    games_list = Game.objects.all().order_by('-creation_time')  # Ordena os jogos pela data de criação
    return render(request, 'show_games.html', {'games_list': games_list})

def insert_games(request):
    if request.method == "POST":
        summoner_name = request.POST.get('summoner_name')
        search_games_from_riot_api(summoner_name)
        return redirect('success_url')  # Redireciona para uma URL de sucesso após a inserção
    return render(request, 'insert_games.html')