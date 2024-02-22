import requests
from datetime import datetime
from .models import Game, Player


def get_puuid(summoner_name, riot_id, api_key):
    puuid = None
    url_account = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{summoner_name}/{riot_id}?api_key={api_key}"

    response = requests.get(url_account)
    if response.status_code == 200:
        account_info = response.json()
        player_obj = Player(
            summoner_name=account_info['gameName'],
            riot_id=account_info['tagLine'],
            puuid=account_info['puuid'],
        )
        player_obj.save()
        puuid = account_info['puuid']
        if puuid is None:
            print('Puuid não foi preenchido.')
    else:
        print("Erro na requisição get.")
    return puuid

def search_games_from_puuid(puuid, api_key):
    url_idmatches = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=20&api_key={api_key}"
    response = requests.get(url_idmatches)
    id_matches = response.json()
    return id_matches

def get_game_data(id_matches, api_key):
    games_data = []  # Lista para armazenar dados de várias partidas
    for id in id_matches:
        url_matchdata = f"https://americas.api.riotgames.com/lol/match/v5/matches/{id}?api_key={api_key}"
        response = requests.get(url_matchdata)
        if response.status_code == 200:
            game_data = response.json()
            games_data.append(game_data)  # Adiciona os dados da partida à lista
    return games_data



def insert_data_from_matches(puuid, api_key, id_matches):
    print('Cheguei até a função de inserir.')
    games_data = get_game_data(id_matches, api_key)

    for game_data in games_data:
        index_mypuuid = game_data['metadata']['participants'].index(puuid)
        participant_data = game_data['info']['participants'][index_mypuuid]

        game_obj = Game(
            game_id=game_data['info']['gameId'],
            champion=participant_data['championName'],
            kills=participant_data['kills'],
            deaths=participant_data['deaths'],
            assists=participant_data['assists'],
            wards=participant_data['wardsPlaced'],
            duracao=game_data['info']['gameDuration'],
            farm=participant_data['totalMinionsKilled'],
            ouro=participant_data['goldEarned'],
            win=participant_data['win'],
            creation_time=datetime.fromtimestamp(game_data['info']['gameCreation'] / 1000),
        )
        game_obj.save()

