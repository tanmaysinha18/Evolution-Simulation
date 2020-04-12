from creature import *
from world import *
from os import system
from pygame import *
from matplotlib import pyplot as plt

def plot_stats(prey_stats,predator_stats):
  global fig,ax1,ax2
  plt.cla()
  plt.plot(prey_stats,label = "Prey")
  plt.plot(predator_stats,label = "Predator")
  plt.legend()
  plt.grid(True)
  plt.pause(0.1)
  

init()
clock=time.Clock()

h=600
w=600
gameDisplay=display.set_mode((h,w))
display.set_caption("Evolution")

crashed = False

world = World()

prey_stats = []
predator_stats = []

number_of_days = 1000
number_of_moves = 100
number_of_food = 1000
number_of_steps = 300
number_of_prey = 200
number_of_predators = 10
number_of_forests = 7
forest_epicenters = [-1]*number_of_forests

world.initialize_creatures(number_of_prey,number_of_predators)

for day in range(0,number_of_days):
  prey_stats.append(world.num_prey)
  predator_stats.append(len(world.predators))
  # world.clear_food()
  steps_taken = 0
  forest_epicenters = world.generate_food(number_of_food,len(forest_epicenters),forest_epicenters)
  # number_of_food=number_of_food-1
  # number_of_food = q
  while len(world.food) > 0 and not crashed and steps_taken < number_of_steps:

    for i in event.get():
      if i.type == KEYDOWN:
        if i.unicode == "q":
          crashed = True
        if i.unicode == "p":
          asdf = input()
        if i.unicode == "h":
          c_speedData=[]
          for c in world.prey:
            c_speedData.append(c.speed)
          plt.cla()
          plt.hist(c_speedData,np.linspace(0,100,100))
          plt.show()
    if crashed:
      exit()

    world.move_creatures()
    world.detect_eat()

    gameDisplay.fill((255,255,255))
    world.print_food(gameDisplay)
    world.print_creatures(gameDisplay)
    display.update()
    clock.tick(60)
    steps_taken = steps_taken + 1
  plot_stats(prey_stats,predator_stats)
  if crashed:
    break
  world.reset_creatures()

plt.grid(True)
plt.show()