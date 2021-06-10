# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 11:59:57 2021

@author: Michael Silva
"""
import pig
import pandas as pd
import pickle
from os import path

from agents import optimus
from agents import primo
from agents import ralph
from agents import maverick
from agents import fred
from agents import ted
from agents import luke
from agents import barry
from agents import athena as p2

n_games_to_play = 1000000
n_games_until_save = 100

player_1 = ralph.Player()
player_2 = p2.Player()

if player_2.is_learner:
    # Full memory file
    memory_file = "./" + player_2.name + ".p"

    if path.exists(memory_file):
        print("Loading Memory")
        memory = pickle.load(open(memory_file, "rb"))
        df = pd.DataFrame.from_dict(memory, orient="index")
        initialize_with = df[0].min()
        player_2 = p2.Player(memory=memory, initialize_with=initialize_with)
    else:
        print("No Memory Found")
        player_2 = p2.Player(initialize_with=0.001)

results = {}
win_rates = []
# Adjust for the same players
player_2_name = player_2.name
if player_2_name == player_1.name:
    player_2_name = player_2_name + " 2"

names = [player_1.name, player_2_name]
n_games_played = 0

print("Playing the game...")
while n_games_played < n_games_to_play:
    game = pig.Game(player_1, player_2)
    game.play()
    winner = game.get_winner()
    winner_name = names[winner]
    results[winner_name] = results.get(winner_name, 0) + 1
    n_games_played += 1

    # Save along the way
    if n_games_played % n_games_until_save == 0:
        """
        n = str(n_games_played).zfill(7)
        save_name = player_1.name + "-" + n + ".p"
        memory = player_2.get_memory()
        pickle.dump(memory, open(save_name, "wb"))
        del(memory)
        """
        wins = results[player_2_name] / sum(results.values())
        win_rates.append({'Games': n_games_played, 'Win Rate': wins})
        #print("Win Rate After " + str(n_games_played) + " Games: " + str(round(wins * 100, 2)) + "%")

print(results)
if player_2.is_learner:
    # Get the player's memory
    memory = player_2.get_memory()
    # Save the memory
    pickle.dump(memory, open(memory_file, "wb"))
    # A brief analysis of the memories
    df = pd.DataFrame.from_dict(memory, orient="index")
    df = df.sort_index()
    df.to_csv(player_1.name+".csv")
    print(df.head())
    # How many states has the player seen?
    print(len(df.index))

    df2 = pd.DataFrame(win_rates)
    df2.to_csv("win_rates.csv", index = False)
print(wins)