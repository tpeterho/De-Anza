import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('data.txt')

x = data[:,0]
y = data[:,1]

def linear(x):
    m = 0.75
    b = 2
    return m * x + b 

n = np.linspace(0,60,50)

plt.plot(n,linear(n))
plt.scatter(x,y)
