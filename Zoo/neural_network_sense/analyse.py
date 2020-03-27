import numpy as np
from prey import Prey
from predator import Predator
from copy import deepcopy
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.patheffects


def prey_sense(prey_blocks, num_prey, numBlocksx, numBlocksy):
    if num_prey>0:
        prey_blocks = deepcopy(prey_blocks)
        avg_direction_vector_pred = np.array([0,0])
        avg_direction_vector_food = np.array([0,0])
        # origin = [0,0]
        fig3, axs = plt.subplots(2,figsize=(8, 8))
        fig3.suptitle('prey sense plots')
        axs[0].set_title('if predator is at (1,0)')
        axs[1].set_title('if food is at (1,0)')
        for i in range(numBlocksx):
          for j in range(numBlocksy):
            for p in prey_blocks[i][j]:
                x = p.compute_nn_food_custom(np.array([0,0,-1,0]))
                avg_direction_vector_pred = avg_direction_vector_pred + x
                y = p.compute_nn_food_custom(np.array([1,0,0,0]))
                avg_direction_vector_food = avg_direction_vector_food + y
# [1    53,204,255]
                axs[0].arrow(0,0,x[0],x[1],color = np.array([153,204,255])/255)

                axs[1].arrow(0,0,y[0],y[1],color = np.array([153,204,255])/255)

        avg_direction_vector_pred = avg_direction_vector_pred/(num_prey+0.0001)
        avg_direction_vector_food = avg_direction_vector_food/(num_prey+0.0001)

        axs[0].arrow(0,0,avg_direction_vector_pred[0], avg_direction_vector_pred[1],color ='r')
        axs[1].arrow(0,0,avg_direction_vector_food[0], avg_direction_vector_food[1],color ='r')   

        plt.show()

def predator_sense(predator_list):
    if len(predator_list)>0:
        predator_list = deepcopy(predator_list)
        avg_direction_vector = np.array([0,0])
        fig2, ax = plt.subplots(figsize=(8, 8))
        fig2.suptitle('predator sense plots')
        ax.set_title('if prey is at (1,0)')
        for p in predator_list:
            x = p.compute_nn_food_custom(np.array([1,0]))
            avg_direction_vector = avg_direction_vector+x
            ax.arrow(0,0,x[0],x[1],color = np.array([153,204,255])/255)

        avg_direction_vector = avg_direction_vector/len(predator_list)
        ax.arrow(0,0,avg_direction_vector[0], avg_direction_vector[1],color ='r')

        plt.show()