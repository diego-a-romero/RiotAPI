import requests
from datetime import datetime
from .models import Game

def search_games_from_riot_api(summoner_name):
    api_key = "RGAPI-53aa8319-d2fd-478c-928c-561bb85311c9"
    url = f"https://americas.api.riotgames.com/lol/match/v4/matches/{summoner_name}?api_key={api_key}"

    response = requests.get(url)
    if response.status_code == 200:
        games_data = response.json()
        for game in games_data['matches']:
            game_obj = Game(
                game_id=game['gameId'],
                champion=game['champion'],
                kills=game['kills'],
                deaths=game['deaths'],
                assists=game['assists'],
                wards=game['wardsPlaced'],
                duracao=game['gameDuration'],
                farm=game['totalMinionsKilled'],
                ouro=game['goldEarned'],
                win=game['win'],
                creation_time=datetime.fromtimestamp(game['gameCreation'] / 1000),
                total_ouro=game['totalGold'],
                total_kills=game['totalKills'],
            )
            game_obj.save()