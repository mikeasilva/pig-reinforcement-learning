# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 11:59:57 2021

@author: Michael Silva
"""


class Player:
    # Maverick targets a user specified threshold
    name = "Maverick"

    def __init__(self, target = 20, plus_or_minus = 3):
        self.points_at_risk = 0
        self.score = 0
        self.target = target
        self.plus_or_minus = plus_or_minus

    def roll_again(self):
        # Stop if close to target or if we have enough points to win the game
        fuzzy_target = self.target - self.plus_or_minus
        if self.points_at_risk <= fuzzy_target or self.score + self.points_at_risk < 100:
            return 1
        self.score += self.points_at_risk
        self.points_at_risk = 0
        return 0

    def observe_roll(self, roll, your_turn):
        # Observe the results of the roll
        if your_turn:
            if roll > 1:
                self.points_at_risk += roll
            else:
                self.points_at_risk = 0
