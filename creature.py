import numpy as np
import matplotlib.pyplot as plt

class creature(starting_pos):
    def __init__(self,starting_pos=[0,0]):
        self.starting_pos=np.array(starting_pos)
        self.health=100
        self.fertility=0
        self.pos=starting_pos
        self.moveflag=True
        self.content=False

    def getPos(self):
        return self.pos

    def move(self,worldSz):
        if(self.moveflag==True):
            self.pos[0]=np.random.randint(-1,2)+self.pos[0]
            self.pos[1]=np.random.randint(-1,2)+self.pos[1]
            if self.pos[0]<0:
                self.pos[0]=0
            if self.pos[0]>=worldSz[0]:
                self.pos[0]=worldSz[0]-1
            if self.pos[1]<0:
                self.pos[1]=0
            if self.pos[1]>=worldSz[1]:
                self.pos[1]=worldSz[1]-1

    def eat(self):
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
        self.pos=starting_pos
