import numpy as np
from prey import *
from predator import *
import numpy.linalg as LA
import random

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
    self.prey = np.array([])
    self.predators = np.array([])
    # self.food = np.array([])
    self.numBlocksx=5
    self.numBlocksy=5
    self.blocksize=np.array([self.x_range//self.numBlocksx,self.y_range//self.numBlocksy])
    self.food=[]
    self.prey_blocks = []
    self.num_prey = 0
    start=0
    for i in range(self.numBlocksx):
      row1 = []
      row2 = []
      for j in range(self.numBlocksy):
        row1.append([])
        row2.append([])
      self.food.append(row1)
      self.prey_blocks.append(row2)

  def initialize_creatures(self, number_of_prey,number_of_predator):
    for i in range(0, number_of_prey):
      new_prey = Prey([random.uniform(0,self.x_range),random.uniform(0,self.y_range)])
      pos = new_prey.getPos()
      self.num_prey += 1
      self.prey_blocks[pos[0]//self.blocksize[0]][pos[1]//self.blocksize[1]].append(new_prey)
      # self.prey=np.hstack((self.prey,Prey([150,300])))

    for i in range(0, number_of_predator):
      self.predators=np.hstack((self.predators,Predator([random.uniform(0,self.x_range),random.uniform(0,self.y_range)])))


  def clear_food(self):
    self.food=[]
    for i in range(self.numBlocksx):
      row = []
      for j in range(self.numBlocksy):
        row.append([])
      self.food.append(row)        
        
  def generate_food(self, num_trees, num_forests, forest_epicenter = [-1,-1]):
    if len(forest_epicenter)>0 and forest_epicenter[0]==-1:
      forest_epicenter = [(np.random.uniform(0, self.x_range), np.random.uniform(0, self.y_range)) for i in range(num_forests)]
    if np.random.uniform(0,1)>0.9:
      print("New forest generated!!")
      num_forests = num_forests+1  
      forest_epicenter.append((np.random.uniform(0, self.x_range), np.random.uniform(0, self.y_range)))
    
    if np.random.uniform(0,1)>0.9:
      if num_forests>0:
        print("A forest is no longer able to sustain itself!!")
        num_forests = num_forests-1
        forest_epicenter.pop(np.random.randint(0,len(forest_epicenter)))
      if num_forests == 0:
        print("There will be scarcity of food. No one will survive!!")  
      
    
    forest_density = np.array([(np.random.randint(1,num_trees//num_forests)) for i in range(num_forests)])
    remaining = num_trees - np.sum(forest_density)
    forest_density = (remaining//num_forests)*np.ones(forest_density.shape)+forest_density
    
    for i in range(num_forests):
      for j in range(int(forest_density[i])):
        foodnew=[(forest_epicenter[i][0]+np.random.normal(0,50))%self.x_range,(forest_epicenter[i][1]+np.random.normal(0,50))%self.y_range]
        self.food[int(foodnew[0])//self.blocksize[0]][int(foodnew[1])//self.blocksize[1]].append(Food(foodnew))
    return forest_epicenter

  def move_creatures(self):
    for i in range(self.numBlocksx):
      for j in range(self.numBlocksy):
        for prey in self.prey_blocks[i][j]:
          # if prey.moveflag:
            old_pos = np.array(prey.getPos())
            prey.move((self.x_range,self.y_range))
            new_pos = prey.getPos()
            old_block = [old_pos[0]//self.blocksize[0],old_pos[1]//self.blocksize[1]]
            new_block = [new_pos[0]//self.blocksize[0],new_pos[1]//self.blocksize[1]]
            # print("new_block--> ",new_block)
            # print("old_block--> ",old_block)
            if new_block[0] != old_block[0] or new_block[1] != old_block[1]:
              self.prey_blocks[old_block[0]][old_block[1]].remove(prey)
              self.prey_blocks[new_block[0]][new_block[1]].append(prey)
    
    for predator in self.predators:
      # if predator.moveflag:
        predator.move((self.x_range,self.y_range))


  def print_food(self,gameDisplay):
    for x in range(self.numBlocksx):
      for y in range(self.numBlocksy):
        for food in self.food[x][y]:
          if not food.eaten:
            pos = food.getPos()
            draw.rect(gameDisplay,food.color,Rect(pos[0],pos[1],food.size,food.size))


  def print_creatures(self,gameDisplay):
    self.num_prey = 0
    for i in range(self.numBlocksx):
      for j in range(self.numBlocksy):
        for creature in self.prey_blocks[i][j]:
          creature.draw(gameDisplay)
          self.num_prey += 1
    for creature in self.predators:
      creature.draw(gameDisplay)

  def reset_creatures(self):
    new_prey = []
    for i in range(self.numBlocksx):
      for j in range(self.numBlocksy):
        for creature in self.prey_blocks[i][j]:
          if not creature.content:
            self.prey_blocks[i][j].remove(creature)

        for creature in self.prey_blocks[i][j]:
          if creature.fertility > 0:
            p = Prey(creature.getPos(),creature.speed+np.random.randint(-10,10),prey_sense = creature.prey_sense + np.random.uniform(-2,2), run_from_predator_sense = creature.run_from_predator_sense+ np.random.uniform(-2,2))
            pos = p.getPos()
            # print("New prey added")
            self.prey_blocks[i][j].append(p)
          creature.newIteration()


    # self.prey = np.array(new_prey)
    new_predators = []
    for creature in self.predators:
      if creature.fertility > 0:
        new_predators.append(Predator(creature.getPos(),creature.speed+np.random.randint(-10,10),prey_sense = creature.prey_sense+ np.random.uniform(-2,2)))

      if creature.content:
        new_predators.append(creature)

      creature.newIteration()

    self.predators = np.array(new_predators)


  def detect_eat(self,gameDisplay):
    for i in range(self.numBlocksx):
      for j in range(self.numBlocksy):
        for creature in self.prey_blocks[i][j]:
          pos=creature.getPos()
          creatureXblock=pos[0]//self.blocksize[0]
          creatureYblock=pos[1]//self.blocksize[1]
          eaten_indices = []
          mindist = 1000
          minpos = [0,0]
          for idx,fud in zip(range(len(self.food[creatureXblock][creatureYblock])),self.food[creatureXblock][creatureYblock]):
            if creature.fertility<100:
              foodpos=fud.getPos()
              dist = LA.norm(foodpos-np.array(pos))
              if dist<mindist:
                mindist = dist
                minpos = foodpos 
              if dist<creature.size+2:
                creature.eat()
                eaten_indices.append(idx)
                creature.towards_prey_velocity = np.array([0,0])
            if idx == len(self.food[creatureXblock][creatureYblock])-1 and creature.fertility<100:
              creature.towards_prey_velocity = (np.array(minpos) - np.array(pos))/LA.norm(np.array(minpos) - np.array(pos))
          self.food[creatureXblock][creatureYblock] = np.ndarray.tolist(np.delete(self.food[creatureXblock][creatureYblock],eaten_indices,0))

    for predator in self.predators:
      pos=predator.getPos()
      creatureXblock=pos[0]//self.blocksize[0]
      creatureYblock=pos[1]//self.blocksize[1]
      eaten_indices = []
      mindist = 1000
      minpos = np.array([0,0])
      minprey = 0
      for idx,prey in zip(range(len(self.prey_blocks[creatureXblock][creatureYblock])),self.prey_blocks[creatureXblock][creatureYblock]):
        if predator.fertility<100 or predator.fertility>=0:
          foodpos=prey.getPos()
          dist = LA.norm(foodpos-np.array(pos))
          print(len(self.prey_blocks[creatureXblock][creatureYblock]))
          if dist<mindist:
                mindist = dist
                minpos = foodpos
                minprey = prey
          if dist<predator.size+2:
            # print(prey)
            predator.eat()
            eaten_indices.append(idx)
            predator.towards_prey_velocity = np.array([0,0])
        
        if idx == len(self.prey_blocks[creatureXblock][creatureYblock])-1:
          print(mindist)
          predator.towards_prey_velocity = (np.array(minpos) - np.array(pos))/LA.norm(np.array(minpos) - np.array(pos))
          minprey.away_from_predator_velocity = (-np.array(pos) + np.array(minpos))/LA.norm(-np.array(pos) + np.array(minpos))
          draw.circle(gameDisplay,(1,0,0),minpos,10)
          print(minpos)
        # print(eaten_indices)

      self.prey_blocks[creatureXblock][creatureYblock] = np.ndarray.tolist(np.delete(self.prey_blocks[creatureXblock][creatureYblock],eaten_indices,0))
