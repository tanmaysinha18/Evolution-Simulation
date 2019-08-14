import numpy as np
import matplotlib.pyplot as plt
from pygame import *

class Creature():
    def __init__(self,starting_pos=[0,0]):
        self.starting_pos=np.array(starting_pos)
        self.health = 500
        self.fertility=0
        self.pos=np.array(starting_pos)
        self.moveflag=True
        self.content=False
        self.theta = 2 * np.pi * np.random.rand() - np.pi
        self.speed = 50
        self.color = (255,9,0)
        self.size = 5

    def getPos(self):
        return self.pos

    def move(self,worldSz):
        if(self.moveflag==True):
            self.health = self.health - 1
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
        # print("EATEN")
        if (self.fertility<100):
            if (self.content==False):
                 self.content=True
            else:
                self.moveflag=False
                self.fertility=100
    
    def newIteration(self):
        if (self.content==True):
            self.health=100
            self.content=False
        self.fertility=0
        self.moveflag=True
        self.pos=self.starting_pos