# Generated by Django 5.0.2 on 2024-02-21 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riotapp', '0004_game_assists_game_deaths_game_duracao_game_farm_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='puuid',
            field=models.CharField(max_length=78),
        ),
    ]
