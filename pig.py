# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 11:59:57 2021

@author: Michael Silva
"""
import random
import matplotlib.pyplot as plt
import matplotlib.cm as cm

class Game:
    def __init__(self, player_1, player_2, verbose=False):
        self.players = [player_1, player_2]
        self.player_index = 0
        self.history = []
        self.points_at_risk = 0
        self.score = [0, 0]
        self.verbose = verbose
        self.winner = None

    def play(self):
        self.players[0].new_game()
        self.players[1].new_game()
        while max(self.score) < 100:
            # Figure out who's the current player
            current_player = self.players[self.player_index]
            other_player = self.players[(1 if self.player_index == 0 else 0)]
            # Set the player's turn flag to True
            it_is_the_players_turn = True
            # Loop until it's not the player's turn
            first_roll = True
            while it_is_the_players_turn:
                # Get their decision
                if first_roll or current_player.roll_again() == 1:
                    first_roll = False
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
                        + " (Player "
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
                    # Create an image for the reinforcement learner
                    #Image(self.score[0], self.score[1], self.points_at_risk)
                else:
                    it_is_the_players_turn = False
            # Adjust the score
            self.score[self.player_index] += self.points_at_risk
            self.debug("Score: " + str(self.score[0]) + " to " + str(self.score[1]))
            # Notify the players of the score
            self.players[0].score_update(self.score[0], self.score[1])
            self.players[1].score_update(self.score[1], self.score[0])
            # Change the current player
            self.player_index = 1 if self.player_index == 0 else 0
            
            self.points_at_risk = 0
        self.winner = 0 if self.score[0] >= 100 else 1
        self.debug(
            "Player "
            + str(self.winner + 1)
            + " Wins with "
            + str(self.score[self.winner])
            + " Points!"
        )

    def debug(self, message):
        if self.verbose:
            print(message)

    def get_winner(self):
        return self.winner


class Image:
    # Creates an image representation of the game
    def __init__(self, player_1_score, player_2_score, points_at_risk):
        cmap = cm.get_cmap('jet')
        normalized_points_at_risk = points_at_risk / 105
        plt.axis('square')
        plt.xlim(-5, 110)
        plt.ylim(-5, 110)
        ax = plt.gca()
        ax.axes.xaxis.set_visible(False)
        ax.axes.yaxis.set_visible(False)
        colors = [cm.jet(x) for x in range(0, 106)]
        self.game_image = plt.scatter([player_1_score], [player_2_score], color=[cmap(normalized_points_at_risk)])
        # Save the image
        plt.savefig('pig.png')
        
    def show(self):
        self.game_image.show()
        
    
        
        