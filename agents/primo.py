# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 11:59:57 2021

@author: Michael Silva
"""


class Player:
    # Primo is a player that rolls once and then ends their turn
    name = "Primo"

    def __init__(self):
        self.n_roll = 0

    def roll_again(self):
        if self.n_roll == 0:
            return 1
        self.n_roll = 0
        return 0

    def observe_roll(self, roll, your_turn):
        if your_turn:
            self.n_roll += 1
