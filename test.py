# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 11:59:57 2021

@author: Michael Silva
"""
import pig
from agents import optimus
from agents import primo
from agents import ralph
from agents import maverick

n_games_to_play = 5000

player_1 = maverick.Player(50)
player_1 = primo.Player()
player_2 = optimus.Player()

results = {}
names = [player_1.name, player_2.name]
n_games_played = 0

while n_games_played < n_games_to_play:
    game = pig.Game(maverick.Player(50), optimus.Player())
    game.play()
    winner = game.get_winner()
    winner_name = names[winner]
    results[winner_name] = results.get(winner_name, 0) + 1
    n_games_played += 1

print(results)
