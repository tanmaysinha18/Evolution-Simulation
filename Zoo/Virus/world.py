import numpy as np
from creature import *
import numpy.linalg as LA

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
    # self.food = np.array([])
    self.numBlocksx=50
    self.numBlocksy=50
    self.blocksize=np.array([self.x_range//self.numBlocksx,self.y_range//self.numBlocksy])
    self.food=[]

    #Virus characteristics
    self.virus = {"infectivity":0.07,"life":10,"mortality":0.02}

    start=0
    for i in range(self.numBlocksx):
      row = []
      for j in range(self.numBlocksy):
        row.append([])
      self.food.append(row)

  def initialize_creatures(self, number):
    self.initial_creatures = 100
    for i in range(0, number):
      # self.creatures.append(Creature([0,np.random.randint(0,self.y_range)]))
      # self.creatures=np.hstack((self.creatures,Creature([0,np.random.randint(0,self.y_range)])))
      self.creatures=np.hstack((self.creatures,Creature(starting_pos=np.random.randint(1,599,size = 2))))
    unfortunate_creature = np.random.randint(0,len(self.creatures))
    self.creatures[unfortunate_creature].infect()
    pos = self.creatures[unfortunate_creature].getPos()
    self.infected_tiles = [[pos[0],pos[1],0]]
    self.uninfected_creatures = self.initial_creatures - 1
    self.infected_creatures = 1

  def move_creatures(self):
    for creature in self.creatures:
      if creature.moveflag:
        creature.move((self.x_range,self.y_range))
        if creature.infected:
          if creature.infect_surroundings(self.virus["infectivity"]) and not self.is_tile_infected(creature.getPos()):
            pos = creature.getPos()
            t = [pos[0],pos[1],0]
            self.infected_tiles.append(t)
        else:
          # if self.infected_tiles.any(creature.getPos()):
          if self.is_tile_infected(creature.getPos()):
            p = np.random.uniform()
            if p < 10*self.virus["infectivity"]:
              creature.infect()

  def is_tile_infected(self,pos):
    for tiles in self.infected_tiles:
      if tiles[0] == pos[0] and tiles[1] == pos[1]:
        return True
    return False

  def print_virus(self,gameDisplay):
    for tile in self.infected_tiles:
      pos = (tile[0],tile[1])
      draw.rect(gameDisplay,(125,0,0),(pos[0],pos[1],5,5))

  def reset_virus(self):
    new_set = []
    for tile in self.infected_tiles:
      pos = (tile[0],tile[1])
      tile[2] += 1
      if tile[2] <= self.virus["life"]:
        new_set.append(tile)
    self.infected_tiles = new_set
    # print(new_set)


  def print_creatures(self,gameDisplay):
    for creature in self.creatures:
      draw.circle(gameDisplay,creature.color,creature.getPos(),creature.size)

  def reset_creatures(self):
    new_creatures = []
    for creature in self.creatures:
      if creature.fertility > 0:
        new_creatures.append(Creature(creature.getPos(),creature.speed))
      creature.pos = np.array(creature.init_pos)
      if creature.infected:
        creature.attempt_to_kill(self.virus["mortality"])
        creature.infected_days += 1
        if creature.infected_days > self.virus["life"]:
          creature.disinfect()
      if creature.content:
        new_creatures.append(creature)

      creature.newIteration()

    self.infected_creatures = 0
    self.creatures = np.array(new_creatures) 
    for creature in self.creatures:
      if creature.infected:
        self.infected_creatures += 1
