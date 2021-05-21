from scipy import random
import numpy as np
import matplotlib.pyplot as plt

i = 1 # set a value for current in Amperes (A)
B = 2 # set a value for magnetic field in Tesla (T)
R = 1 # set length of wire in meters (m)
a1 = -R # set left end point of straight wire
b1 = R # set right end point of straight wire
a2 = 0 # set left end point of curved wire
b2 = np.pi # set end point of curved wire
N = 1000 # set number of intervals N


def f(x):
    return 1
    
def g(x):
    return np.sin(x)

# generate an array of all zeroes 
array1 = np.zeros(N)
array2 = np.zeros(N)
    
# change each entry in array to a random number between a and b
for i in range(N):
    array1[i] = random.uniform(a1,b1)
    array2[i] = random.uniform(a2,b2)

# compute summation over all random numbers in array
integral_straight = 0.0
integral_semicirc = 0.0

for i in array1:
    integral_straight += f(i)
    
for i in array2:
    integral_semicirc += g(i)

# compute the average value for each 
# contribution of force from each wire
straight = ((b1-a1)/float(N)) * integral_straight 
semicirc = ((b2-a2)/float(N)) * integral_semicirc

# calculate the net force by subtraction
f_net = - i * B * straight + i * B * R * semicirc
    
print('The net force is %0.06f' % f_net, 'N')
