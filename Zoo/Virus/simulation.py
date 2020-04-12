from creature import *
from world import *
from os import system
from pygame import *
from matplotlib import pyplot as plt

def plot_stats(uninfected_creature_stats,infected_creature_stats,dead_creature_stats):
  plt.cla()
  plt.plot(uninfected_creature_stats,color = "blue",label = "Uninfected")
  plt.plot(infected_creature_stats,color = "red",label = "Infected")
  plt.plot(dead_creature_stats,color = (0.3,0.3,0.3),label = "Dead")
  plt.legend(loc = "upper right")
  plt.grid(True)
  plt.pause(0.01)
  

init()
clock=time.Clock()

h=600
w=600
gameDisplay=display.set_mode((h,w))
display.set_caption("Virus")

crashed = False

world = World()

uninfected_creature_stats = []
infected_creature_stats = []
dead_creature_stats = []

number_of_days = 1000
number_of_moves = 100
# number_of_food = 100
number_of_steps = 300
number_of_creatures = 100

world.initialize_creatures(number_of_creatures)

for day in range(0,number_of_days):
  infected_creature_stats.append(world.infected_creatures)
  uninfected_creature_stats.append(len(world.creatures) - world.infected_creatures)
  dead_creature_stats.append(number_of_creatures - len(world.creatures))
  # world.clear_food()
  steps_taken = 0
  # world.generate_food(number_of_food)
  # number_of_food=number_of_food-1
  number_of_food = max(5,int(np.random.normal(100,25)))
  while not crashed and steps_taken < number_of_steps:

    for i in event.get():
      if i.type == KEYDOWN:
        if i.unicode == "q":
          crashed = True
        if i.unicode == "p":
          asdf = input()
        # if i.unicode=="s":
        #   plt.grid(True)
        #   plt.plot(creature_stats)
        #   plt.show()
    if crashed:
      exit()
      
    world.move_creatures()

    gameDisplay.fill((255,255,255))
    world.print_creatures(gameDisplay)
    world.print_virus(gameDisplay)
    display.update()
    # if steps_taken%2 == 0:
    #   image.save(gameDisplay, 'images/day_'+str(day)+'_'+str(steps_taken)+'.png')
    clock.tick(60)
    steps_taken = steps_taken + 1
  plot_stats(uninfected_creature_stats,infected_creature_stats,dead_creature_stats)
    
  world.reset_creatures()
  world.reset_virus()

# plt.grid(True)
# plt.plot(creature_stats)
# plt.show()