import numpy as np
from numpy import random
from matplotlib import pyplot as mp
import csvdatabase as csvdb
# S(t) = S(0)e^((drift -0.5vol^2)t+vol*B(t))

#drift mu - expected return per unit of time
# vol sigma - volatility
# B(t) ~ N(0,t)(normally distributed with mean 0 and variance t)

class stochasticprocess:
    def __init__(self,T,n_steps, seed = None):
        self.T = T
        self.n_steps = n_steps
        self.dt = T/n_steps
        self.time_grid = np.linspace(0,T,n_steps+1)
        
        if seed is not None:
            np.random.seed(seed)
        
class geometricbrownian(stochasticprocess):
    def __init__(self,S0:float,mu:float,sigma:float,T:float,n_steps:int,seed=None):
        super().__init__(T,n_steps,seed)
        self.S0 = S0
        self.mu = mu
        self.sigma = sigma
    def simplepath(self):
        #dS(t) = muS(t)dt + sigmaS(t)dB(t)
        # dB(t) = sqrt(t) * N(0,dt)
        dB = np.sqrt(self.dt)* np.random.randn(self.n_steps)
        B = np.zeros(self.n_steps+1)
        B[1:] = np.cumsum(dB)
        drift = (self.mu - 0.5*self.sigma**2) * self.time_grid
        diffusion = self.sigma * B
        S = self.S0 * np.exp(drift+diffusion)
        return S
    def multiplesimplepath(self,num)->np.array:
        grid = np.zeros((num, self.n_steps+1))
        for n in range(num):
            S = self.simplepath()
            grid[n-1] = S
            
        grid = np.transpose(grid)
        return grid
    def get_time_grid(self):
        return self.time_grid

def predict_for_data(ticker:str,time_days:float, num_of_data:int,mu:float,sigma:float,num_of_sim:int):
    data = csvdb.get_close_data(ticker)
    seed = random.randint(0,99999999)
    n = geometricbrownian(data[len(data)-1],mu,sigma,1,num_of_data,seed)
    g = n.multiplesimplepath(num_of_sim)
    data_x = len(data[6700:])
    new_time_grid = n.get_time_grid()
    for i in range(len(n.get_time_grid())):
        new_time_grid[i-1] = new_time_grid[i-1]*time_days + data_x-1
    mp.plot(new_time_grid,g)
    mp.plot(data[6700:])
    mp.show()
            
class arthmeticbrownian(stochasticprocess):
    def __init__(self,S0:float,mu:float,sigma:float,T:float,n_steps:int,seed=None):
        super().__init__(T,n_steps,seed)
        self.S0 = S0
        self.mu = mu
        self.sigma = sigma
    def simplepath(self):
        dB = np.sqrt(self.dt)* np.random.randn(self.n_steps)
        B = np.zeros(self.n_steps+1)
        B[1:] = np.cumsum(dB)
        S = self.S0 + (self.mu* self.time_grid) + self.sigma*B