import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 

%matplotlib notebook # jupyter code for interactive plotting

def VoltFinder(dims,iters,h): # routine to map the voltage across a plate
    V = np.zeros((dims, dims))   

    V[:,0] = 100.0                              # fixed potential line at 100V

    for iter in range(iters):                       # iterations over algorithm
        for i in range(h, dims-h):                                                
            for j in range(h,dims-h): V[i,j] = 0.25*(V[i+h,j]+V[i-h,j]+V[i,j+h]+V[i,j-h])  # equation to find the potential at each point with specified granularity
    x = range(0, dims)
    y = range(0, dims)
    X, Y = np.meshgrid(x,y)
    return X, Y, V # x and y grid coords paired with the voltages at those points

def functz(V):                                  # Function returns V(x, y)
    z = V[X,Y]                        
    return z

X, Y, V = VoltFinder(100,1000,1)
    
Z = functz(V)                          
fig = plt.figure()                              # Create figure
ax = Axes3D(fig, auto_add_to_figure=False)      # Plots axes
fig.add_axes(ax)
ax.plot_wireframe(Y, X, Z, color = 'r')         # red wireframe
ax.set_xlabel('X')                              # label axes
ax.set_ylabel('Y')
ax.set_zlabel('Potential U')
plt.show()  

# contour plot to go along with the meshgrid

plt.figure()
plt.contour(X,Y,Z,linewidths=3)
plt.colorbar(label='V - volts')
plt.ylabel('x - [m]')
plt.xlabel('y - [m]')
plt.title('Electrostatic Potential Contours')
plt.show()

# Testing out the difference in iterations necessary when using a tolerance to track the improvement in the Voltage's solution 

def VoltFinder2(dims,iters,lim):
    V = np.zeros((dims, dims)) 
    

    V[:,0] = 100.0                              # fixed potential line at 100V

    for iter in range(iters):
        Vdumb = np.zeros((dims, dims)) + V # dummy list to store previous voltages as we continue to converge towards a solution
        for i in range(1, dims-1):                                                
            for j in range(1,dims-1): V[i,j] = 0.25*(V[i+1,j]+V[i-1,j]+V[i,j+1]+V[i,j-1])
        check = abs(Vdumb - V) # if the difference between the current solution and the previous is under a certain value, this process is halted
        flags = []
        for ind in check: # scanning the differences between this iteration and the previous iteration
            for val in ind:
                if val > lim:
                    flags.append(1)
        if len(flags) == 0:
            print(iter)
            break
                
           
        

VoltFinder2(100,1000,0.05)
VoltFinder2(100,1000,0.1)
VoltFinder2(100,1000,0.2)
VoltFinder2(100,1000,0.5)
VoltFinder2(100,1000,0.8)
VoltFinder2(100,1000,0.9)
