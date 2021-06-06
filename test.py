# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 11:59:57 2021

@author: Michael Silva
"""
import pig
from agents import optimus
from agents import primo 
from agents import ralph

game = pig.Game(ralph.Player(), primo.Player())
game.play()