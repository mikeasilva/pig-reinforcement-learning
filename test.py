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
from agents import fred
from agents import ted

player_1 = optimus.Player()
player_2 = ted.Player(initialize_with=0.01, learn_from_others=True)

game = pig.Game(player_1, player_2)
game.play()

print(game.get_winner())
print(player_2.get_memory())