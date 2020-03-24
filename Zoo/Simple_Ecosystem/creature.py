import numpy as np
import matplotlib.pyplot as plt
from pygame import *

class Creature():
    '''
    Creature object class.
    '''

    def __init__(self,starting_pos=[0,0],speed=np.random.randint(10,20),size=np.random.randint(1,10)):
        def colorfunc(speed):
            if speed<10:
                return (10,255,0)
            elif speed<=50:
                return (speed*5,2550/speed,0)
            else:
                return (255,0,0)
        self.starting_pos=np.array(starting_pos)
        self.health = 100
        self.fertility=0
        self.pos=np.array(starting_pos)
        self.moveflag=True
        self.content=False
        self.theta = 2 * np.pi * np.random.rand() - np.pi
        self.size = size 
        if speed<0:
            self.speed = 2
        else:
            self.speed=speed
        self.color = colorfunc(self.speed)
        self.size = 5

    def getPos(self):
        return self.pos

    def move(self,worldSz):
        '''
        Move function for the creature. 
        Each creature moves by randomly perturbing it's angle by a few radians, and then moving in the direction 
        determined by that angle.
        '''
        if(self.moveflag==True):
            
            # decrease in health with every step
            self.health = self.health -self.speed/50
            if self.health<=0:
                self.moveflag=False
            self.theta = self.theta + 0.5*(np.random.rand()) - 0.25
            velocity = self.speed * np.array([np.cos(self.theta),np.sin(self.theta)])
            self.pos = self.pos + velocity * 0.1
            

            # self.pos[0]=np.random.randint(-1,2)+self.pos[0]
            # self.pos[1]=np.random.randint(-1,2)+self.pos[1]
            if self.pos[0]<0:
                self.pos[0]=0
                self.theta = self.theta - np.pi/2 
            
            if self.pos[0]>=worldSz[0]:
                self.pos[0]=worldSz[0]-1
                self.theta = np.pi - self.theta

            if self.pos[1]<0:
                self.pos[1]=0
                self.theta = self.theta - np.pi/2


            if self.pos[1]>=worldSz[1]:
                self.pos[1]=worldSz[1]-1
                self.theta = -self.theta


            self.pos = np.array([int(self.pos[0]),int(self.pos[1])])
    
    def eat(self):
        '''
        Function to eat a given food. Called when a collision between food and creature is detected.
        '''
        # print("EATEN")
        if (self.fertility<100):
            if (self.content==False):
                 self.content=True
            else:
                self.moveflag=False
                self.fertility=100
    
    def newIteration(self):
        '''
        Setup the creature for the new iteration.
        '''
        if (self.content==True):
            self.health=100
            self.content=False
        self.fertility=0
        self.moveflag=True
        # self.pos=self.starting_pos