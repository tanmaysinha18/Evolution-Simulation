from creature import *
from nn_model import model_simple_predator

class Predator(Creature):
  def __init__(self,starting_pos=[0,0],
    speed=np.random.randint(10,20),
    size=np.random.randint(1,10),
    sense = np.random.uniform(0,20),
    weights_food = np.random.uniform(-1,1,(2,6))):

    super(Predator,self).__init__(starting_pos,speed,size)
    self.color = (0,0,0)
    self.nn_food = model_simple_predator(weights_food)

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

  def compute_nn_food_speed(self):
    x = self.towards_prey_velocity
    x = self.nn_food.forward(x.reshape(2,1))
    x = x/(np.linalg.norm(x)+0.001)
    return x.reshape(2,)

  def compute_nn_food_custom(self,x):
    x = self.nn_food.forward(x.reshape(2,1))
    x = x/(np.linalg.norm(x)+0.001)
    return x.reshape(2,)

  def move(self,worldSz):
    if(self.moveflag==True or (self.away_from_predator_velocity[0]!=0 and self.away_from_predator_velocity[1]!=0)):
        
        # decrease in health with every step
        self.health = self.health -self.speed/75
        if self.health<=0:
            self.moveflag=False
        # self.theta = self.theta + 0.5*(np.random.rand()) - 0.25
        self.velocity = self.velocity+np.random.normal(0,1,self.velocity.shape) + self.sense*self.compute_nn_food_speed()
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
