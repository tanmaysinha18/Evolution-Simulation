import numpy as np
from creature import *

class Food():
  def __init__(self,pos):
    self.pos = pos
    self.value = 100
    self.size = 5
    self.color = (0,255,0)
    self.eaten = False

  def getPos(self):
    return self.pos

class World():
  def __init__(self):
    self.x_range = 600
    self.y_range = 600
    self.grid = np.array([[" " for i in range(0,self.y_range)] for j in range(0,self.x_range)])
    self.creatures = np.array([])
    self.food = np.array([])

  def initialize_creatures(self, number):
    for i in range(0, number):
      # self.creatures.append(Creature([0,np.random.randint(0,self.y_range)]))
      # self.creatures=np.hstack((self.creatures,Creature([0,np.random.randint(0,self.y_range)])))
      self.creatures=np.hstack((self.creatures,Creature([300,300])))

  def clear_food(self):
    self.food = np.array([])

  def generate_food(self, number):
    for i in range(0,number):
      self.food=np.hstack((self.food,Food(np.array([np.random.randint(0,self.x_range),np.random.randint(0,self.y_range)]))))
      # self.food.append(Food(np.array[np.random.randint(0,self.x_range),np.random.randint(0,self.y_range)]))
      self.food = sorted(self.food,key = lambda x:x.pos[0])

  def move_creatures(self):
    for creature in self.creatures:
      if creature.moveflag:
        creature.move((self.x_range,self.y_range))


  def print_food(self,gameDisplay):
    for food in self.food:
      if not food.eaten:
        pos = food.getPos()
        draw.rect(gameDisplay,food.color,Rect(pos[0],pos[1],food.size,food.size))


  def print_creatures(self,gameDisplay):
    for creature in self.creatures:
      draw.circle(gameDisplay,creature.color,creature.getPos(),creature.size)

  def reset_creatures(self):
    new_creatures = []
    for creature in self.creatures:
      if creature.fertility > 0:
        new_creatures.append(Creature(creature.getPos(),creature.speed+np.random.randint(-10,10)))

      if creature.content:
        new_creatures.append(creature)

      creature.newIteration()

    self.creatures = np.array(new_creatures)

  def detect_eat(self):
    def nearest(arr,x):
      for i in range(0,len(arr)):
        if arr[i] >= x:
          return i
      
      return -1

    fud=[]
    for f in self.food:
      pos=f.getPos()
      fud.append(pos[0])
    fud=np.array(fud)
    # print(fud)
    for creature in self.creatures:
      
      pos=creature.getPos()
      index = np.searchsorted(fud,pos[0])
      # index = nearest(fud,pos[0])
      # print(fud)
      upperbound=index
      eaten_indices = []
      
      while upperbound<len(fud) and fud[upperbound]<pos[0]+creature.size+2:
      
        if(np.linalg.norm(self.food[upperbound].pos-pos)<creature.size + self.food[0].size):
          creature.eat()
          self.food[upperbound].eaten = True
          eaten_indices.append(upperbound)
      
        upperbound=upperbound+1
      lowerbound=index-1
      
      while lowerbound>=0 and fud[lowerbound]>pos[0]-creature.size:
      
        if(np.linalg.norm(self.food[lowerbound].pos-pos)<creature.size + self.food[0].size):
          creature.eat()
          self.food[lowerbound].eaten=True
          eaten_indices.append(lowerbound)
      
        lowerbound=lowerbound-1

      self.food = np.delete(self.food,eaten_indices,0)
      fud = np.delete(fud,eaten_indices,0)