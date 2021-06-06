# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 11:59:57 2021

@author: Michael Silva
"""
import pig
from agents import optimus
from agents import primo 

game = pig.Game(primo.Player(), optimus.Player())
game.play()