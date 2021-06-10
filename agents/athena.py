# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 06:23:15 2021

@author: Michael Silva
"""
import random


class Player:
    # Athena is a player that makes a decision based on probabilities.
    # She observes the game to formulate her probabilities.
    name = "Athena"
    is_learner = True

    def __init__(self, memory={}, initialize_with=0.001, learn_from_others = True):
        self.initialize_with = initialize_with
        self.memory = memory
        self.my_score = 0
        self.opponents_score = 0
        self.points_at_risk = 0
        self.seen_state = {}
        self.learn_from_others = learn_from_others

    def roll_again(self):
        state_memory = self.get_state_memory()
        # Force first roll
        if state_memory == [0, 0, 0]:
            return 1
        
        probability_of_success = state_memory[1] / sum(state_memory)

        if probability_of_success == 0.5:
            # No clear winner so flip a coin
            decision = 1 if random.random() < probability_of_success else 0
        else:
            # Go with the more likely choice
            decision = 0 if probability_of_success < 0.5 else 1

        if decision == 0:
            self.points_at_risk = 0
            state_key = self.get_game_state_key()
        return decision

    def observe_roll(self, roll, your_turn):
        state_key = self.get_game_state_key(your_turn)
        if your_turn or self.learn_from_others:
            state_memory = self.get_state_memory(your_turn)
            self.seen_state[state_key] = self.seen_state.get(state_key, 0) + 1
            # Update the reward or punishment memory
            if roll == 1:
                # Remember the loss
                state_memory[0] = state_memory[0] + self.points_at_risk
                self.points_at_risk = 0
            else:
                # Remember the win
                state_memory[1] = state_memory[1] + roll
                self.points_at_risk += roll
            self.memory[state_key] = state_memory


    def score_update(self, my_score, opponent_score):
        self.my_score = my_score
        self.opponents_score = opponent_score
        self.points_at_risk = 0

    def get_game_state(self, for_fred = True):
        if for_fred:
            return [self.my_score, self.opponents_score, self.points_at_risk]
        else:
            return [self.opponents_score, self.my_score, self.points_at_risk]

    def get_game_state_key(self, for_fred = True):
        return "-".join(str(i) for i in self.get_game_state(for_fred=for_fred))

    def get_state_memory(self, for_fred = True):
        game_state_key = self.get_game_state_key(for_fred=for_fred)
        return self.memory.get(
            game_state_key, [self.initialize_with, self.initialize_with]
        )  # [don't roll, roll]

    def get_memory(self):
        return self.memory

    def new_game(self):
        self.my_score = 0
        self.opponents_score = 0
        self.points_at_risk = 0
