from creature import *
from nn_model import model_simple_prey

class Prey(Creature):
  def __init__(self,starting_pos=[0,0],
    speed=np.random.randint(10,20),
    size=np.random.randint(1,10),
    sense = np.random.uniform(0,20), 
    weights_food = np.random.uniform(-1,1,(4,10))):

    super(Prey,self).__init__(starting_pos,speed,size)
    self.color = (255,255,0)
    self.nn_food = model_simple_prey(weights_food)

  def draw(self,gameDisplay):
    draw.circle(gameDisplay,self.color,self.getPos(),self.size)
    draw.circle(gameDisplay,self.speed_color,self.getPos(),self.size//2)

  def eat(self):
    # print("Prey has eaten")
    if (self.fertility<100):
      if (self.content==False):
        self.content=True
      else:
        self.moveflag=False
        self.fertility=100
  
  def compute_nn_food_speed(self):
    x = np.hstack((self.towards_prey_velocity, self.away_from_predator_velocity))
    x = self.nn_food.forward(x.reshape(4,1))
    x = x/(np.linalg.norm(x)+0.001)
    return x.reshape(2,)

  def compute_nn_food_custom(self,x):
    x = self.nn_food.forward(x.reshape(4,1))
    x = x/(np.linalg.norm(x)+0.001)
    return x.reshape(2,)


  def move(self,worldSz):
    if(self.moveflag==True or (self.away_from_predator_velocity[0]!=0 and self.away_from_predator_velocity[1]!=0)):
        
        # decrease in health with every step
        self.health = self.health -self.speed/50
        if self.health<=0:
            self.moveflag=False

        self.velocity = self.velocity+np.random.normal(0,1,self.velocity.shape) + self.sense*self.compute_nn_food_speed()

        self.away_from_predator_velocity = np.array([0,0])
        self.towards_prey_velocity = np.array([0,0])
      
        multiplier = self.speed/(np.linalg.norm(self.velocity)+0.0001)
      
        self.velocity = multiplier*self.velocity
        self.pos = self.pos + self.velocity * 0.06
        
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