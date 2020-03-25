import numpy as np
import matplotlib.pyplot as plt
from pygame import *

class Creature():
    def __init__(self,starting_pos=[0,0],speed=np.random.randint(10,20),size=np.random.randint(0,10), prey_sense = np.random.uniform(0,20), run_from_predator_sense = np.random.uniform(0,20)):
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
        self.prey_sense = prey_sense
        self.run_from_predator_sense = run_from_predator_sense
        self.moveflag=True
        self.content=False
        self.theta = 2 * np.pi * np.random.rand() - np.pi
        self.velocity = np.random.uniform(-1,1,(2,))
        self.away_from_predator_velocity = np.array([0,0])
        self.towards_prey_velocity = np.array([0,0])
        self.size = size
        if speed<0:
            self.speed = 2
        else:
            self.speed=speed
        self.speed_color = colorfunc(self.speed)
        self.size = 5

    def getPos(self):
        if np.isnan(self.pos[0]) or np.isnan(self.pos[1]):
            self.pos[0]=300
            self.pos[1]=300
        return [int(self.pos[0]),int(self.pos[1])]

    def move(self,worldSz):
        # if(self.moveflag==True or (self.away_from_predator_velocity[0]!=0 and self.away_from_predator_velocity[1]!=0)):
            
            # decrease in health with every step
            self.health = self.health -self.speed/50
            if self.health<=0:
                self.moveflag=False


            '''
                here,
                velocity = random velocity + alpha x velocity(towards prey) + beta x velocity(away from predator)

                and,
                alpha = sense of the creature to detect prey (food is the prey for prey)
                beta = sense of the creature to detect predator (predator has 0 velocity(away from predator))

                alpha and beta are the elements that grow genetically
            '''   
            self.velocity = self.velocity+np.random.normal(0,1,self.velocity.shape) + self.prey_sense*self.towards_prey_velocity +self.run_from_predator_sense*self.away_from_predator_velocity
            self.away_from_predator_velocity = np.array([0,0])
            self.towards_prey_velocity = np.array([0,0])
            multiplier = self.speed/np.linalg.norm(self.velocity)
            self.velocity = multiplier*self.velocity
            self.pos = self.pos + self.velocity * 0.06
            

            # self.pos[0]=np.random.randint(-1,2)+self.pos[0]
            # self.pos[1]=np.random.randint(-1,2)+self.pos[1]
            if self.pos[0]<=0:
                self.pos[0]=0
                self.velocity[0] = -self.velocity[0] 
            
            if self.pos[0]>=worldSz[0]:
                self.pos[0]=worldSz[0]-1
                self.velocity[0] = -self.velocity[0] 


            if self.pos[1]<0:
                self.pos[1]=0
                self.velocity[1] = -self.velocity[1]


            if self.pos[1]>=worldSz[1]:
                self.pos[1]=worldSz[1]-1
                self.velocity[1] = -self.velocity[1]


            # self.pos = np.array([int(self.pos[0]),int(self.pos[1])])
    
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
        # self.pos=self.starting_pos