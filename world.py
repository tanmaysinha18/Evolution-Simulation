import numpy as np

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

  def print_world(self):
    for y in self.grid:
      for i in y:
        print(i,end="")
      print()