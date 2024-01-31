import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integr8

# Using the equation of motion which describes a Van Der Pol Oscillator for non-linear oscillations (shown as newstate[1] in the code), a numerical solution can be found for a problem that cannot be solved analyitcal for large epsilon

def a(ist,t): # function that provides a numerical result for the Van Der Pol equation given a starting displacement and velocity
    eps = 1
    newstate[0] = ist[1] # velocity
    newstate[1] = -ist[0] - eps*(ist[0]**2-1)*ist[1] # acceleration using the Van Der Pol equation
    return newstate
    
    
    
N = 75
t, h = np.linspace(0,8*np.pi,N,retstep=True) # steps to integrate over
ist = ([0.5,0.]) # starting position and velocity respectively
newstate = np.zeros(2)

vev = integr8.odeint(a,ist,t) # using scipy's integrate function 
plt.plot(t,vev[:,0]) # plot of the evolution of the oscillator's displacement over time
plt.ylabel('displacement x[m]')
plt.title('Displacement vs Time')
plt.xlabel('time t(s)')
plt.show()
plt.plot(t,vev[:,1]) # plot of the evolution of the oscillator's velocity over time
plt.ylabel('time t(s)')
plt.xlabel('velocity v[m/s]')
plt.title('Velocity vs Time')
plt.show()

plt.title('van der Pol Oscillator') # Plot overlaying the velocity over time onto the position over time in order to analyze the validity of this result
plt.plot(t,vev[:,0],label='displacement x[m]')
plt.plot(t,vev[:,1],label='velocity v[m/s]')
plt.ylabel('time t(s)')
plt.legend()

plt.scatter(vev[:,0],vev[:,1],c=t) # plot of the phase space of the non-linear oscillator over time
plt.title('Phase Space X vs. V')
plt.xlabel('displacement x[m]')
plt.ylabel('velocity v[m/s]')
plt.colorbar()

initlt = [([1.0,0.0]),([2.0,0.0]),([3.0,0.0])] # Plotting the phase space over different starting starting postions in order to analyze the asymptotic limits of the oscillator
for sc in initlt:
    y = integr8.odeint(a,sc,t)
    plt.scatter(y[:,0],y[:,1],c=t)
    plt.title('Phase Space X (x0 = %d) vs. V' % sc[0])
    plt.xlabel('displacement x[m]')
    plt.ylabel('velocity v[m/s]')
    plt.colorbar()
    plt.show()
