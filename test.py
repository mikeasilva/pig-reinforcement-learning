# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 11:59:57 2021

@author: Michael Silva
"""
import pig
import pickle
import pandas as pd

from agents import optimus
from agents import primo
from agents import ralph
from agents import maverick
from agents import fred
from agents import ted
from agents import barry
from agents import athena

n_games_to_play = 1000
n_games_played = 0

# Basic settings
initialize_with = 0.01
memory = {}
# Load memory files
#memory = pickle.load(open("./Ted/Ralph.p", "rb"))
#df = pd.DataFrame.from_dict(memory, orient="index")
#initialize_with = df[0].min()

player_1 = optimus.Player()
#player_2 = ted.Player(memory=memory, initialize_with=initialize_with, learn_from_others=True)
player_2 = fred.Player()

wins = [0, 0]
while n_games_played < n_games_to_play:
    game = pig.Game(player_1, player_2)
    game.play()
    wins[game.get_winner()] += 1
    n_games_played += 1

# Print the results
print(player_1.name + " won " + str(wins[0])+ " times and " + player_2.name + " won "+str(wins[1])+" times.")
#print(player_2.get_memory())