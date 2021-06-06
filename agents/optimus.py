# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 11:59:57 2021

@author: Michael Silva
"""

class Player:
    # Optimus targets 20, the optimal strategy
    name = "Optimus"

    def __init__(self):
        self.points_at_risk = 0
        self.score = 0

    def roll_again(self):
        # Since 20 is the optimal time to stop, we will stop when the points are 18 to 24 or if we have enough points to win the game 
        if self.points_at_risk <= 18 or self.score + self.points_at_risk < 100:
            return 1
        self.score += self.points_at_risk
        self.points_at_risk = 0
        return 0
    
    def observe_roll(self, roll):
        # Observe the results of the roll
        if roll > 1:
            self.points_at_risk += roll
        else:
            self.points_at_risk = 0