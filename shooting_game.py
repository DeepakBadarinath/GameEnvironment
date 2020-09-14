# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 15:21:39 2020

@author: deepa
"""
import numpy as np

class AmongUs2:
    """contains info about game at a given point of time"""
    def __init__(self,citizens_list,angels_list,devils_list):
        self.citizens_list=citizens_list
        self.angels_list=angels_list
        self.devils_list=devils_list
        

class Game_Board:
    pass

def play():
    pass
    

class Character:
    char_no=0
    moves=['up','right','left','down']
    movement=0.1
    
    def __init__(self,name='Citizen',ammo=10,health=100,upgrades=[],position=[0,0]):
        self.name=name
        self.ammo=ammo
        self.health=health
        self.upgrades=upgrades
        self.position=position
        Character.char_no=Character.char_no+1
        print("Char_no is now",Character.char_no)
    
    def move(self,move):
        if move=='up' and self.position[1]-Character.movement>0:
            self.position[1]-=Character.movement
        elif move=='down'and self.position[1]+Character.movement<10:
            self.position[1]+=Character.movement
        elif move=='right'and self.position[0]+Character.movement<10:
            self.position[0]+=Character.movement
        elif move=='left'and self.position[0]-Character.movement>0:
            self.position[0]-=Character.movement
        return self.position
    
    def shoot(self,aim):
        distance=np.linalg.norm(self.position-aim)
        if "Good_Shooting" in self.upgrades:
            return np.random.multivariate_normal(np.array(self.position,(distance*np.identity(2))/100))
        elif "Intoxicated" in self.upgrades:
            return np.random.multivariate_normal(np.array(self.position,(distance*np.identity(2))*100))
        else:
            return np.random.multivariate_normal(np.array(self.position,(distance*np.identity(2))))
        self.ammo-=1
    

class Angel(Character):
    angel_no=0
    def __init__(self,name='Angel',revive_no=2,chakra=1,caught=False,ammo=10,health=100,upgrades=[],position=[0,0]):
        super().__init__(ammo,health,upgrades,position)
        self.revive_no=revive_no
        self.name = name
        self.caught=caught
        self.chakra=1
        Angel.angel_no+=1
    
    def revive(self,patient):
        if self.revive_no<=0:
            return False
        patient.health=100
    
    def give_chakra(self,player):
        if self.chakra<=0:
            return False
        player.upgrades.append("Chakra")
        
    
    

c1 = Character(name='Jai',position=[1,1])
print(c1.position)


angel= Angel(name='Angelina')
angel.give_chakra(c1)
#print(c1.upgrades)
#print(angel.ammo)
print(angel.char_no)
angel.name='Fionna'
print(angel.name)











