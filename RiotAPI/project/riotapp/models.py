from django.db import models

# Create your models here.
class Player(models.Model):
    summoner_name = models.CharField(max_length=16, unique=True)
    level = models.IntegerField(max_length=5)
    rank = models.CharField(max_length=20)

    def __str__(self):
        return self.summoner_name

class Game(models.Model):
    game_id = models.CharField(max_length=100)
    champion = models.CharField(max_length=50)
    kills = models.IntegerField(max_length=3)
    deaths = models.IntegerField(max_length=3)
    assists = models.IntegerField(max_length=3)
    wards = models.IntegerField(max_length=3)
    duracao = models.IntegerField(max_length=5)
    farm = models.IntegerField(max_length=5)
    ouro = models.IntegerField(max_length=6)
    win = models.BooleanField()
    creation_time = models.DateTimeField()
    total_ouro = models.IntegerField(max_length=7)
    total_kills = models.IntegerField(max_length=5)

    def __str__(self):
        return f"{self.game_id} - {self.champion}"
