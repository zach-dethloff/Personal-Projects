import numpy as np
import matplotlib.pyplot as plt

def V(x,p,vreturn): # anharmonic function taking in a value for x, the exponent p, and a list for the intial values of the given potential's first derivative
    k = 2
    vReturn[0] = x[1] # intial value for the velocity
    vReturn[1] = -k*pow(x[0],p-1) # intial value of the first derivative
    
def Vp(x,p): # anharmonic potential
    k = 2
    return -1/p*k*pow(x,p)

def Kp(v): # converting numerical solution of the potential into a kinetic energy to ensure energy is conserved
    return v**2/2


p = [2,4,8] # different values for the exponential

for val in p:
    j=0 #iterator for assigning results of integration to corresponding lists
    l=1 #subplot positioning
    b = 10 # final time
    n = 100 #step number                                          
    ydumb = np.zeros(2) # dummy list to rotate values through
    y = np.zeros(2) # list for previous values of the solution to the function
    tt=np.zeros(n+2) # list of time intervals which corresponds to the solution
    yy1=np.zeros(n+2) # solutions for the positions of the oscillator
    yy2=np.zeros(n+2) # solutions for the velocities of the oscillator
    vReturn = np.zeros(2) # empty list to store solutions of the first derivative
    k1 = np.zeros(2) # placeholder values while the solution converges
    k2 = np.zeros(2)
    k3 = np.zeros(2)
    k4 = np.zeros(2)
    y[0] = 1.5 # intial conditions
    y[1] = 0.0
    t = 0 # start time
    tt[0]=t
    yy1[0]=y[0] # starting position
    yy2[0]=y[1] # starting velocity
    h = b/n; # step size
    while (t < b):     # Runge-Kutta until iterations have been maximized                                           
        if ( (t + h) > b ): 
            h = b - t                           
        V(y, val, vReturn)                            
        k1[0] = h*vReturn[0];  k1[1] = h*vReturn[1]   
        for i in range(0, 2): ydumb[i] = y[i] + k1[i]/2. 
        V(ydumb, val, vReturn) 
        k2[0] = h*vReturn[0];  k2[1] = h*vReturn[1] 
        for i in range(0, 2):  ydumb[i] = y[i] + k2[i]/2. 
        V(ydumb, val, vReturn)
        k3[0] = h*vReturn[0];  k3[1] = h*vReturn[1] 
        for i in range(0, 2): ydumb[i] = y[i] + k3[i] 
        V(ydumb, val, vReturn) 
        k4[0] = h*vReturn[0];   k4[1] = h*vReturn[1]  
        for i in range(0, 2): 
            y[i] = y[i] + (k1[i] + 2.*(k2[i] + k3[i]) + k4[i])/6.
        j+=1 
        t+=h
        tt[j]=t
        yy1[j]=y[0]  
        yy2[j]=y[1]
        
    plt.figure(figsize=(10,6)) 
    plt.subplot(3,3,l) 
    plt.plot(tt,yy1,'r') # plot for position vs. time
    plt.grid(True)
    plt.title('x vs. t for p = %d' % val)
    plt.ylabel('x[m]')
    plt.xlabel('t[s]')
    plt.subplot(3,3,l+1)
    plt.plot(tt,yy2,'b') # plot for velocity vs. time
    plt.grid(True)
    plt.xlabel('t[s]')
    plt.ylabel('v(m/s)')
    plt.title('v vs. t for p = %d' % val)
    plt.subplot(3,3,l+2)
    plt.plot(Vp(yy1,val),Kp(yy2)) # plot of potential vs. kinetic, should be linear
    plt.xlabel('V(x)')
    plt.ylabel('K(v)')
    plt.grid(True)
    plt.title('Energy conservation')
    plt.show()
    l+=3

