# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 11:59:57 2021

@author: Michael Silva
"""
import random


class Player:
    # "Lucky" Luke randomly decides what to do
    name = "Luke"

    def roll_again(self):
        return 1 if random.random() < 0.5 else 0

    def observe_roll(self, roll, your_turn):
        do_nothing = True

    def score_update(self, my_score, opponent_score):
        do_nothing = True

    def new_game(self):
        do_nothing = True
