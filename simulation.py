from creature import *
from world import *
from os import system
from pygame import *
from matplotlib import pyplot as plt

init()
clock=time.Clock()

h=600
w=600
gameDisplay=display.set_mode((h,w))
display.set_caption("Evolution")

crashed = False

world = World()

creature_stats = []

number_of_days = 15
number_of_moves = 100
number_of_food = 100
number_of_steps = 150
number_of_creatures = 50

world.initialize_creatures(number_of_creatures)


for day in range(0,number_of_days):
  world.reset_creatures()
  creature_stats.append(len(world.creatures))
  world.clear_food()
  steps_taken = 0
  world.generate_food(number_of_food)
  while len(world.food) > 0 and not crashed and steps_taken < number_of_steps:
    for i in event.get():
      if i.type == KEYDOWN:
        if i.unicode == "q":
          crashed = True
        if i.unicode == "p":
          asdf = input()
    
    world.move_creatures()
    world.detect_eat()

    gameDisplay.fill((255,255,255))
    world.print_food(gameDisplay)
    world.print_creatures(gameDisplay)
    display.update()
    clock.tick(60)
    steps_taken = steps_taken + 1
    # print(steps_taken)
  c_speedData=[]
  for c in world.creatures:
    c_speedData.append(c.speed)
  plt.hist(c_speedData,np.linspace(0,100,100))
  plt.show()

plt.grid(True)
plt.plot(creature_stats)
plt.show()