# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 11:59:57 2021

@author: Michael Silva
"""

class Player:
    # "Reckless" Ralph rolls until he gets 100+ points then quits
    name = "Ralph"

    def __init__(self):
        self.points_at_risk = 0

    def roll_again(self):
        if self.points_at_risk < 100:
            return 1
        self.points_at_risk = 0
        return 0
    
    def observe_roll(self, roll):
        if roll > 1:
            self.points_at_risk += roll
        else:
            self.points_at_risk = 0