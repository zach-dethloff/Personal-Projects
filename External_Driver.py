import numpy as np
import matplotlib.pyplot as plt

# This finds the solution, given a potential, to a driven oscillator for position and velocity using the 4th Order Runge-Kutta Method

def V2(x,t,w,vReturn,Fo=50): # potential solutions for first order derivation and starting velocity
    k = 2
    vReturn[0] = x[1]
    vReturn[1] = -k*x[0] + Fo*np.sin(w*t)
    


a = 0.
b = 10. # final time
n = 100  # steps in time
w = 1.8 # natural frequency of the system
ydumb = np.zeros(2) # placeholder list to rotate values through
y = np.zeros(2) # intial conditions of position and velocity
tt=np.zeros(n+2) # list for times to go along with solutions
yy1=np.zeros(n+2) # solutions for position
yy2=np.zeros(n+2) # solutions for velocity
vReturn = np.zeros(2) # dummy list for potential function outputs
k1 = np.zeros(2) # lists that will hold increasingly more accurate to the solutions
k2 = np.zeros(2)
k3 = np.zeros(2)
k4 = np.zeros(2)
y[0] = 1.5 # initial position
y[1] = 0.0 # initial velocity
t = a # starting time = 0
tt[0]=t 
yy1[0]=y[0]
yy2[0]=y[1]
h = (b-a)/n; # step for the integration

j=0
while (t < b): # integration algorithm                                                            
    if ( (t + h) > b ): 
        h = b - t                                         
    V2(y,t,w, vReturn)                              
    k1[0] = h*vReturn[0];  k1[1] = h*vReturn[1]   
    for i in range(0, 2): ydumb[i] = y[i] + k1[i]/2. 
    V2(ydumb, t + h/2., w, vReturn) 
    k2[0] = h*vReturn[0];  k2[1] = h*vReturn[1] 
    for i in range(0, 2):  ydumb[i] = y[i] + k2[i]/2. 
    V2(ydumb, t + h/2., w, vReturn)
    k3[0] = h*vReturn[0];  k3[1] = h*vReturn[1] 
    for i in range(0, 2): ydumb[i] = y[i] + k3[i] 
    V2(ydumb, t + h, w, vReturn) 
    k4[0] = h*vReturn[0];   k4[1] = h*vReturn[1]  
    for i in range(0, 2): 
        y[i] = y[i] + (k1[i] + 2.*(k2[i] + k3[i]) + k4[i])/6.
    j+=1 
    t+=h
    tt[j]=t
    yy1[j]=y[0]  
    yy2[j]=y[1]

plt.figure(figsize=(10,6))                         
plt.subplot(2,1,1)                    
plt.plot(tt,yy1,'r') # position vs. time plot
plt.grid(True)
plt.ylabel('x[m]')
plt.xlabel('t[s]')
plt.title('Oscillations of a Driven Harmonic Oscillator (Fo = 50)')
plt.subplot(2,1,2)
plt.plot(tt,yy2,'b') # velocity vs. time plot
plt.grid(True)
plt.xlabel('t[s]')
plt.ylabel('v[m/s]')
plt.show()
