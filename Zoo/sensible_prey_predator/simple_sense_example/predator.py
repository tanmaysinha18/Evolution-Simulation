from creature import *

class Predator(Creature):
  def __init__(self,starting_pos=[0,0],speed=np.random.randint(10,20),size=np.random.randint(1,10),prey_sense = np.random.uniform(50,100)):
    super(Predator,self).__init__(starting_pos,speed,size)
    self.color = (0,0,0)

  def draw(self,gameDisplay):
    draw.circle(gameDisplay,self.color,self.getPos(),self.size)
    draw.circle(gameDisplay,self.speed_color,self.getPos(),self.size//2)

  def eat(self):
    if (self.fertility<100):
      if (self.content==False):
        self.content=True
      else:
        self.moveflag=False
        self.fertility=100
