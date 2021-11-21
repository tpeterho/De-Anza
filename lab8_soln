import numpy as np
import matplotlib.pyplot as plt

# set initial values

m = 0.1 #kg
k = 1000.0 # N/m
x0 = 1.0
v0 = 0.0 # m/s
time = 1.0 # seconds

# Numerical Setup

dt = 0.00001 # time step in seconds
n = int(round(time/dt))

t = np.zeros([n])
x = np.zeros([n])
v = np.zeros([n])

# Initialize values (set initial conditions)

t[0] = 0.0
x[0] = x0
v[0] = v0

# Solve the equations

for i in range(n-1):
    F = -k*x[i] - 0.05*v[i]*abs(v[i])
    a = F / m
    v[i+1] = v[i] + a*dt
    x[i+1] = x[i] + v[i+1]*dt
    t[i+1] = t[i] + dt
    
plt.plot(t,x)
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.title('Spring-mass Oscillation under Damped Force')
