import numpy as np
from creature import *

class Food():
  def __init__(self,pos):
    self.pos = pos
    self.value = 100

  def getpos(self):
    return self.pos

class World():
  def __init__(self):
    self.x_range = 45
    self.y_range = 45
    self.grid = np.array([[" " for i in range(0,self.y_range)] for j in range(0,self.x_range)])
    self.creatures = np.array([])
    self.food = np.array([])

  def print_world(self):
    for y in self.grid:
      for i in y:
        print(i,end="")
      print()

  def initialize_creatures(self, number):
    for i in range(0, number):
      # self.creatures.append(Creature([0,np.random.randint(0,self.y_range)]))
      self.creatures=np.hstack((self.creatures,Creature([0,np.random.randint(0,self.y_range)])))

  def generate_food(self, number):
    for i in range(0,number):
      self.food=np.hstack((self.food,Food(np.array([np.random.randint(0,self.x_range),np.random.randint(0,self.y_range)]))))
      # self.food.append(Food(np.array[np.random.randint(0,self.x_range),np.random.randint(0,self.y_range)]))

  def move_creatures(self):
    for creature in self.creatures:
      if creature.moveflag:
        pos = creature.getPos()
        self.grid[pos[0]][pos[1]] = " "
        creature.move((self.x_range,self.y_range))
        pos = creature.getPos()
        self.grid[pos[0]][pos[1]] = "C"