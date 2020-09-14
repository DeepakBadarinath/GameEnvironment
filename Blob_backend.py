# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 07:55:13 2020

@author: deepa
"""

import numpy as np
import random
import pygame

class BlobGame():
    GRID_SIZE=[10,10]
    OBS_SPACE=GRID_SIZE
    ''' {0 : 'up', 1 : 'right', 2 : 'down', 3 : 'left'}'''
    ACTION_SPACE=[[0,1],[1,0],[0,-1],[-1,0]]
    TIME_REWARD=-0.1
    WIN_REWARD=0.5
    LOOSE_REWARD=-0.7
    
    def __init__(self,state):
        #state[0] = player location
        #state[1] =  food location
        # state[2] = rel enemy location
        self.state=state
    
    
    @classmethod
    def create_game(cls):
        '''Creates a blob_game'''
        player=Blob(Blob.get_random_location(BlobGame.GRID_SIZE))
        enemy=Blob(Blob.get_random_location(BlobGame.GRID_SIZE))
        food=Blob(Blob.get_random_location(BlobGame.GRID_SIZE))
        state=[player.location]+[food.location]+[enemy.location]
        Game=BlobGame(state)
        return Game
    
    
    @staticmethod
    def get_relative_states(v0,v1,v2):
        return [list(np.array(v1)-np.array(v0)),list(np.array(v2)-np.array(v0))]

    @staticmethod
    def finished_and_win(v1,v2):
        if v1==[0,0]:
            return True,True
        elif v2 == [0,0]:
            return True,False
        return False,None
    
    @staticmethod
    def in_grid(vector,GRID_SIZE):
        if GRID_SIZE[0]>vector[0]>=0 and GRID_SIZE[1]>vector[1]>=0:
            return True
        else:
            return False
    
    @staticmethod
    def get_reward(win,time_reward,win_reward,loose_reward):
        reward=time_reward
        if win==True:
            reward+=win_reward
        elif win==False:
            reward+=loose_reward
        return reward
    
    def move(self,action):
        new_p_location=np.array(self.state[0]) + np.array(action)
        if BlobGame.in_grid(new_p_location,BlobGame.GRID_SIZE):
            self.state[0]=list(new_p_location)
        return self.state[0]
            
    
    def step(self,action):
        '''The RL function, returns the relative new_state,reward,DONE'''
        '''action is a list'''
        self.move(action)
        relative_states=BlobGame.get_relative_states(self.state[0],self.state[1],self.state[2])
        (done,win)=BlobGame.finished_and_win(relative_states[0],relative_states[1])
        reward=BlobGame.get_reward(win,BlobGame.TIME_REWARD,BlobGame.WIN_REWARD,BlobGame.LOOSE_REWARD)
        return (relative_states,reward,done)
    
    def reset(self):
        self.state=BlobGame.create_game().state
        return BlobGame.get_relative_states(self.state[0],self.state[1],self.state[2])
        
'''    def render(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
                pygame.quit()
        screen.fill((0,0,0))
        
    
 '''   
    
class Blob():
    def __init__(self,location):
        self.location=location
    
    @staticmethod
    def get_random_location(GRID_SIZE):
        return [np.random.randint(GRID_SIZE[0]),np.random.randint(GRID_SIZE[1])]
    
    @staticmethod
    def get_random_action(Actions):
        x=np.random.randint(len(Actions))
        print(Actions[x])
        return Actions[x]

