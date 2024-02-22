from django.db import models

# Create your models here.
class Player(models.Model):
    summoner_name = models.CharField(max_length=16)
    riot_id = models.CharField(max_length=50)
    puuid = models.CharField(max_length=78)

    def __str__(self):
        return self.summoner_name

class Game(models.Model):
    game_id = models.CharField(max_length=100)
    champion = models.CharField(max_length=50)
    kills = models.IntegerField()
    deaths = models.IntegerField()
    assists = models.IntegerField()
    wards = models.IntegerField()
    duracao = models.IntegerField()
    farm = models.IntegerField()
    ouro = models.IntegerField()
    win = models.BooleanField()
    creation_time = models.DateTimeField()

    def __str__(self):
        return f"{self.game_id} - {self.champion}"
