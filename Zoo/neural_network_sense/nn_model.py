import numpy as np
"""
Simple model class for prey:

    4 input neurons:
        2 corresponding to the vector away from the closest predator
        2 corresponding to the vector towards the closest food
    4x2 hidden layers
    2 output neurons corresponding to the direction of sense velocity prey should take

Takes input as the weights for neural-net
"""

class model_simple_prey():
    def __init__(self, weights = np.random.uniform(-1,1,(4,10))):
        self.weights = weights
    
    def forward(self,x):
        '''
            x is a 4x1 vector
        '''
        x = np.tanh(self.weights[:,:4].T.dot(x))
        x = np.tanh(self.weights[:,4:8].T.dot(x))
        x = np.tanh(self.weights[:,8:].T.dot(x))
        return x

    def get_weights(self):
        return self.weights

    # def mutate(self):
    #     return self.weights + np.random.normal(0,1,self.weights.shape)


"""
Simple model class for predator:

    
    2 input neurons corresponding to the vector towards the closest prey
    2x2 hidden layers
    2 output neurons corresponding to the direction of sense velocity predator should take

Takes input as the weights for neural-net
"""

class model_simple_predator():
    def __init__(self, weights = np.random.uniform(-1,1,(2,6))):
        self.weights = weights
    
    def forward(self,x):
        '''
            x is a 4x1 vector
        '''
        x = np.tanh(self.weights[:,:2].T.dot(x))
        x = np.tanh(self.weights[:,2:4].T.dot(x))
        x = np.tanh(self.weights[:,4:].T.dot(x))
        return x

    def get_weights(self):
        return self.weights

    def mutate(self):
        return self.weights + np.random.normal(0,1,self.weights.shape)