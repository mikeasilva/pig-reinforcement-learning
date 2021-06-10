# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 18:02:13 2021

@author: Michael Silva
"""
import random


class Player:
    # Ted is a player that makes a decision based on probabilities on the
    # action to take based on the points at risk
    name = "Ted"
    is_learner = True

    def __init__(self, memory={}, initialize_with=0.001, learn_from_others = False):
        self.initialize_with = initialize_with
        self.memory = memory
        self.points_at_risk = 0
        self.seen_state = {}
        self.learn_from_others = learn_from_others

    def roll_again(self):
        state_memory = self.get_state_memory()
        # Force roll first turn
        if self.points_at_risk == 0:
            return 1
        probability_of_success = state_memory[1] / sum(state_memory)
        # Determine if Fred should roll like flipping a biased coin
        decision = 1 if random.random() < probability_of_success else 0
        if decision == 0:
            self.points_at_risk = 0
        return decision

    def observe_roll(self, roll, your_turn):
        state_key = self.points_at_risk
        if your_turn or self.learn_from_others:
            state_memory = self.get_state_memory()
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
        self.points_at_risk = 0

    def get_state_memory(self):
        game_state_key = self.points_at_risk
        return self.memory.get(
            game_state_key, [self.initialize_with, self.initialize_with]
        )  # [don't roll, roll]

    def get_memory(self):
        return self.memory

    def new_game(self):
        self.points_at_risk = 0

