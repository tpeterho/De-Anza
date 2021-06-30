import matplotlib.pyplot as plt
import numpy as np

# Load data file here
data = np.loadtxt("resistance_data.txt")

# define x and y data by separating columns of data
# here, n = length of column x
x = data[:,0]
y = data[:,1]
n = len(x)

#define sum function 
def sum_func(array):
    asum = 0
    for i in array:
        asum += i
    return asum

#define function for linear regression
def R(a,b,k):
    numerator = k*sum_func(a*b) - sum_func(a)*sum_func(b)
    denominator = k*sum_func(a ** 2) - sum_func(a)**2
    return numerator / denominator

#define a linear function for resistance V = IR
def V(I):
    return I * R(x,y,n)

# begin setting up a figure for our plot 
plt.figure()
plt.xlabel("Current (A)")
plt.ylabel("Voltage (V)") 
plt.title("Current-Voltage Plot")

#create a scatter plot using x and y data points
plt.scatter(x,y)

#create a line plot here based on function defined above for V
I = np.linspace(0,10, n)

plt.plot(I,V(I), color='k')

# inserts equation V = IR into plot
plt.text(6, 10, r'$V =$%0.3f * I' % R(x,y,n), fontsize=15)

plt.show()
