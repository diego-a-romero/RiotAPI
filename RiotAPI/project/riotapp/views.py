from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Game
from .riotdata import get_puuid, search_games_from_puuid, get_game_data, insert_data_from_matches
from .forms import PlayerForm


def show_games(request):
    games = Game.objects.all().order_by('-creation_time')[:20]
    return render(request, 'show_games.html', {'games': games})

def insert_games(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            summoner_name = form.cleaned_data['summoner_name']
            riot_id = form.cleaned_data['riot_id']
            api_key = "RGAPI-22eaf9d9-c0e2-45a9-8a26-d38dd74a7c2c"

            puuid = get_puuid(summoner_name, riot_id, api_key)
            print(puuid)

            if puuid:
                puuid = get_puuid(summoner_name, riot_id, api_key)
                id_matches = search_games_from_puuid(puuid, api_key)
                game_data = get_game_data(id_matches, api_key)
                insert_data_from_matches(puuid, api_key, id_matches)
                pass

            return redirect('show_games')
    else:
        form = PlayerForm()

    return render(request, 'insert_games.html', {'form': form})
