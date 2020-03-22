# Simple_Ecosystem

### Simulation Parameters (= Default Values)
- number_of_days = 100 (number of days you want the simulation to run)
- number_of_moves = 100 (no use as of now)
- number_of_food = 100 (number of food particles that spawn before the day starts)
- number_of_steps = 300 (number of moves each creature gets each day)
- number_of_creatures = 100 (number of Creatures that spawn on the first day)

### Key Bindings
- q - Exit the current active tab (either the graph or the simulation)
- p - Pause. (To resume the simulation, type something and press enter. This needs to be improved in later versions)
- h - A Histogram appears which shows the number of creatures with a particular speed
- s - Show population v/s number of days graph

### Comment/Uncomment
- uncomment line 38 ``` # world.clear_food()``` to delete left over food particles of the previous day. Current setting allows the unused food to be used the next day.
- uncomment line 41 ``` # number_of_food=number_of_food-1 ``` to reduce the count of food particles spawned everyday. This can be used to see which kind of creatures have the highest probabilty of survival.
- comment line 42 ``` number_of_food = max(5,int(np.random.normal(100,25)))``` if you change the number of food in the simulation parameter or want to remove randomness.
