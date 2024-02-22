from django import forms

class PlayerForm(forms.Form):
    summoner_name = forms.CharField(label='Summoner Name', max_length=100)
    riot_id = forms.CharField(label='Riot ID', max_length=100)