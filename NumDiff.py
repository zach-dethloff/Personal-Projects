import numpy as np
import matplotlib.pyplot as plt

def f(x): # Some function that we would like to differentiate numerically for f''(2). Two different differentiation algorithms will be used, and their errors will be compared.
    return x*np.exp(x)

def twop(x,h):
    return (f(x+2*h) - 2*f(x+h) + f(x))/h**2 # forward-difference algorithm

def threep(x,h):
    return (f(x+h) + f(x-h) - 2*f(x))/h**2 # central-difference algorithm

x = 2
h = np.arange(0.5,0.0,-0.05) # step sizes

two = [] # results from forward-difference algorithm
three = [] # results from central-difference algorithm

for val in h:
    two.append(twop(x,val))
    three.append(threep(x,val))
    
exact = 2*np.exp(2) + 2*np.exp(2) # value based off the analytical result of f''(2)
    
print("The exact value is: ", exact)
print("The convergence of the forward difference method: ",two)
print("The convergence of the central difference method: ", three)

errorf = [abs(exact - val)/exact for val in two] # percent error for forward-difference algorithm
errorc = [abs(exact - val)/exact for val in three] # percent error for central-difference algorithm
print(errorf, errorc)

plt.plot(h,errorf,label='Forward Difference Error', color='g') # Plot to visualize how the errors evolve over the range of step sizes and how the two algorithms compare
plt.plot(h,errorc,label='Central Difference Error', color='c')
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.title('Error Comparison for Derivative Methods')
plt.ylabel('Error')
plt.xlabel('h')
