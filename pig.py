# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 11:59:57 2021

@author: Michael Silva
"""
import random


class Game:
    def __init__(self, player_1, player_2, verbose=False):
        self.players = [player_1, player_2]
        self.player_index = 0
        self.history = []
        self.points_at_risk = 0
        self.score = [0, 0]
        self.verbose = verbose

    def play(self):
        while max(self.score) < 100:
            # Figure out who's the current player
            current_player = self.players[self.player_index]
            other_player = self.players[(1 if self.player_index == 0 else 0)]
            # Set the player's turn flag to True
            it_is_the_players_turn = True
            # Loop until it's not the player's turn
            while it_is_the_players_turn:
                # Get their decision
                if current_player.roll_again() == 1:
                    # Roll the die
                    roll = random.randint(1, 6)
                    # Players observe's the results
                    current_player.observe_roll(roll, True)
                    other_player.observe_roll(roll, False)
                    # We log the roll
                    self.history.append((self.player_index, roll))
                    # Print a debug message
                    self.debug(
                        current_player.name
                        + "(Player "
                        + str(self.player_index + 1)
                        + ") rolled a "
                        + str(roll)
                    )
                    # Check to see if they rolled a one
                    if roll == 1:
                        self.points_at_risk = 0
                        it_is_the_players_turn = False
                    else:
                        self.points_at_risk += roll
                else:
                    it_is_the_players_turn = False
            # Adjust the score
            self.score[self.player_index] += self.points_at_risk
            self.debug("Score: " + str(self.score[0]) + " to " + str(self.score[1]))
            # Change the current player
            self.player_index = 1 if self.player_index == 0 else 0
            self.points_at_risk = 0
        winner = 0 if self.score[0] >= 100 else 1
        self.debug(
            "Player "
            + str(winner + 1)
            + " Wins with "
            + self.score[winner]
            + " Points!"
        )

    def debug(self, message):
        if self.verbose:
            print(message)
