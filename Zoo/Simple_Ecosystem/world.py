import numpy as np
from creature import *
import numpy.linalg as LA

class Food():
  '''
  A class for the food object.
  '''

  def __init__(self,pos):
    self.pos = pos
    self.value = 100
    self.size = 5
    self.color = (0,255,0)
    self.eaten = False

  def getPos(self):
    return self.pos

class World():
  '''
  The world object
  '''
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
    start=0
    for i in range(self.numBlocksx):
      row = []
      for j in range(self.numBlocksy):
        row.append([])
      self.food.append(row)        

  def initialize_creatures(self, number):
    '''
    Initialize the world with number of creatures.
    '''
    for i in range(0, number):
      # self.creatures.append(Creature([0,np.random.randint(0,self.y_range)]))
      # self.creatures=np.hstack((self.creatures,Creature([0,np.random.randint(0,self.y_range)])))
      self.creatures=np.hstack((self.creatures,Creature([300,300])))

  def clear_food(self):
    '''
    Clear all the food currently in the world.
    '''
    self.food=[]
    for i in range(self.numBlocksx):
      row = []
      for j in range(self.numBlocksy):
        row.append([])
      self.food.append(row)        
        
  def generate_food(self, number):
    '''
    Generate the food in the world.
    '''

    for i in range(0,number):
      foodnew=[np.random.randint(0,self.x_range),np.random.randint(0,self.y_range)]
      # print(foodnew[1]//self.numBlocksy)
      # print(foodnew[0]//self.numBlocksx)
      self.food[foodnew[0]//self.blocksize[0]][foodnew[1]//self.blocksize[1]].append(Food(foodnew))
      # self.food=np.hstack((self.food,Food(np.array([np.random.randint(0,self.x_range),np.random.randint(0,self.y_range)]))))
      # self.food.append(Food(np.array[np.random.randint(0,self.x_range),np.random.randint(0,self.y_range)]))
      # self.food[foodnew[0]//self.numBlocksx][foodnew[1]//self.numBlocksy] = sorted(self.food[foodnew[0]//self.numBlocksx][foodnew[1]//self.numBlocksy],key = lambda x:x.pos[0])

  def move_creatures(self):
    '''
    Move all the creatures present in the world.
    '''
    for creature in self.creatures:
      if creature.moveflag:
        creature.move((self.x_range,self.y_range))


  def print_food(self,gameDisplay):
    '''
    Print function for the food present; draws a rectangle(representing food) in the gameDisplay.
    '''
    for x in range(self.numBlocksx):
      for y in range(self.numBlocksy):
        for food in self.food[x][y]:
          if not food.eaten:
            pos = food.getPos()
            draw.rect(gameDisplay,food.color,Rect(pos[0],pos[1],food.size,food.size))


  def print_creatures(self,gameDisplay):
    '''
    Print function for the creatures present; draws a circle corresponding to the creature's position in gameDisplay.
    '''
    for creature in self.creatures:
      draw.circle(gameDisplay,creature.color,creature.getPos(),creature.size)

  def reset_creatures(self):
    '''
    Function which determines the number and kinds of creatures present in the next iteration.
    First, checks which creatures survive, then reproduces the creatures which have more than enough food(also
    mutates randomly).
    '''
    new_creatures = []
    for creature in self.creatures:
      if creature.fertility > 0:
        new_creatures.append(Creature(creature.getPos(),creature.speed+np.random.randint(-10,10)))

      if creature.content:
        new_creatures.append(creature)

      creature.newIteration()

    self.creatures = np.array(new_creatures)

  def detect_eat(self):
    '''
    Function that determines whether an animal has eaten any food.
    '''
    def nearest(arr,x):
      for i in range(0,len(arr)):
        if arr[i] >= x:
          return i
      
      return -1

    for creature in self.creatures:
      
      pos=creature.getPos()
      creatureXblock=pos[0]//self.blocksize[0]
      creatureYblock=pos[1]//self.blocksize[1]
      # index = np.searchsorted(fud,pos[0])
      # index = nearest(fud,pos[0])
      # print(fud)
      eaten_indices = []
      for idx,fud in zip(range(len(self.food[creatureXblock][creatureYblock])),self.food[creatureXblock][creatureYblock]):
        foodpos=fud.getPos()
        if LA.norm(foodpos-pos)<creature.size+2:
          creature.eat()
          eaten_indices.append(idx)

      # upperbound=index
      # eaten_indices = []
      
      # while upperbound<len(fud) and fud[upperbound]<pos[0]+creature.size+2:
      
      #   if(np.linalg.norm(self.food[upperbound].pos-pos)<creature.size + self.food[0].size):
      #     creature.eat()
      #     self.food[upperbound].eaten = True
      #     eaten_indices.append(upperbound)
      
      #   upperbound=upperbound+1
      # lowerbound=index-1
      
      # while lowerbound>=0 and fud[lowerbound]>pos[0]-creature.size:
      
      #   if(np.linalg.norm(self.food[lowerbound].pos-pos)<creature.size + self.food[0].size):
      #     creature.eat()
      #     self.food[lowerbound].eaten=True
      #     eaten_indices.append(lowerbound)
      
      #   lowerbound=lowerbound-1

      self.food[creatureXblock][creatureYblock] = np.ndarray.tolist(np.delete(self.food[creatureXblock][creatureYblock],eaten_indices,0))