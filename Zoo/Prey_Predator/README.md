# Prey_Predator
In this scenario, there are two species: 1) Preys that eat food particles and 2) Predators that eat Preys.
Two windows appear when you run the code, one is the simulation visualization window and the other shows plot of populations of both species v/s Day number

### Simulation Parameters (= Default Values)
- number_of_days = 1000 (number of days you want the simulation to run)
- number_of_moves = 100 (no use as of now)
- number_of_food = 200 (number of food particles that spawn before the day starts)
- number_of_steps = 300 (number of moves each creature gets each day)
- number_of_prey = 100 (number of Preys that spawn on the first day)
- number_of_predators = 20 (number of Predators that spawn on the first day) (keep it lower significantly lower than preys, or else one of the species might get extint very soon)

### Key Bindings
- q - Exit the current active tab (either the graph or the simulation)
- p - Pause. (To resume the simulation, type something and press enter. This needs to be improved in later versions)

### Comment/Uncomment
- uncomment line 44 ``` # world.clear_food()``` to delete left over food particles of the previous day. Current setting allows the unused food to be used the next day.
- uncomment line 47 ``` # number_of_food=number_of_food-1 ``` to reduce the count of food particles spawned everyday. This can be used to see which kind of creatures have the highest probabilty of survival.
- comment line 42 ``` number_of_food = max(5,int(np.random.normal(100,25)))``` if you change the number of food in the simulation parameter or want to remove randomness.

Changing ```h``` and ```w``` changes window size, but changing this might cause random behaviour.
