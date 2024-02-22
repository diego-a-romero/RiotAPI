import requests
import json

nickname = input('Qual o seu nickname? ')
riot_tag = input('Qual a Riot Tag (Sem o # ex: BR1):? ')
api_key = "RGAPI-22eaf9d9-c0e2-45a9-8a26-d38dd74a7c2c"
url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{nickname}/{riot_tag}?api_key={api_key}"

api_get_account = requests.get(url)
meu_perfil = api_get_account.json()
meu_perfil_json = json.dumps(meu_perfil, indent=4)

print(meu_perfil_json)
puuid = meu_perfil['puuid']
print(puuid)

url_match = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=20&api_key={api_key}"

api_get_match = requests.get(url_match)
id_partidas = api_get_match.json()
id_partidas_json = json.dumps(id_partidas, indent=4)
print(id_partidas_json)

id = "BR1_2896580214"

url_matchdata = f"https://americas.api.riotgames.com/lol/match/v5/matches/{id}?api_key={api_key}"
response = requests.get(url_matchdata)
match_data = response.json()

index_mypuuid = match_data['metadata']['participants'].index(puuid)
print(index_mypuuid)
print(type(index_mypuuid))

gold = match_data['info']['participants'][index_mypuuid]['goldEarned']
print(gold)
print(type(gold))