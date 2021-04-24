import matplotlib.pyplot as plt
import numpy as np

# Load data file here
data = np.loadtxt("LED_data.txt")

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
def V(i):
    return i * R(x,y,n)

def a(x,y,n):
    numerator = sum_func(x ** 2 * y) * sum_func(y * np.log(y)) - sum_func(x * y)*sum_func(x * y * np.log(y))
    denominator = sum_func(y) * sum_func(x ** 2 * y) - (sum_func(x * y))**2
    return numerator / denominator 

def b(x,y,n):
    numerator = sum_func(y) * sum_func(x * y * np.log(y)) - sum_func(x * y) * sum_func(y * np.log(y))
    denominator = sum_func(y) * sum_func(x ** 2 * y) - (sum_func(x * y)) ** 2
    return numerator / denominator

def I(j,k,v):
    return np.exp(j) * np.exp(k * v) 

# begin setting up a figure for our plot 
plt.figure()
plt.ylabel("Current (A)")
plt.xlabel("Voltage (V)") 
plt.title("Current-Voltage Plot")

#create a scatter plot using x and y data points
plt.scatter(x,y)

#create a line plot here based on function defined above for V
v = np.linspace(0,5, n)

plt.plot(v,I(a(x,y,n),b(x,y,n),v), color='k')
plt.text(0, 40,r'$I =$%0.3f ' % np.exp(a(x,y,n)) + '* $e^{%0.3f * v}$' % b(x,y,n), fontsize=15)

plt.show()
