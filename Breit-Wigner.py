import numpy as np
import matplotlib.pyplot as plt

def F(E): # The Breit Wigner Function, describing the probability of finding a particle of mass M and resonance width Gamma to have an energy E, with the scaling factor described by k.
    return k/((E**2 - M**2)**2 + M**2*Gam**2)

M = 90 # Particle Mass
Gam = 10 # Particle resonance width
gam = np.sqrt(M**2*(M**2+Gam**2)) # Caucy dist necessary for determining the scaling factor

k = 2*np.sqrt(2)*M*Gam*gam/(np.pi*(np.sqrt(M**2 + gam))) # scaling factor
E = np.arange(0,180,1) # range of energies to visualize the distribution

Farr = F(E)

plt.plot(E,Farr, label='Breit-Wigner Function') # Plot of this distribution
plt.legend()
plt.title('Breit-Wigner Distribution vs. Energy')
plt.ylabel('F(E)')
plt.xlabel('Energy (GeV)')

# This function will now be integrated 2 ways, one using the Trapezoidal rule, and the other using the numpy library's trapz function

N = len(E) 
h = (max(E) - min(E))/(N-1) # finding the average value of the energy, since this sits at about the peak of the distribution
tarea = 0 # initial value for the area which will describe the result of our integrated function

def wTrap(i, h): # Trapezoid function, which takes in the current step i, and the average of the Energy                          
    if ( (i == 1) or (i == N) ): 
        wTotal = h/2.0
    else:
        wTotal = h
    return wTotal

for i in range(1, N + 1):
    t = min(E) + (i - 1)*h
    tarea = tarea + wTrap(i, h) * F(t)
  

print("Manually Calculated Integral: ", tarea)

print("Function Calculated Integral: ", np.trapz(F(E), E))

#These agree to about O(-14), which is about where we expect our error to arise due to the nature of machine precision

def simpo(N): # Now we will re-do this numerical integration using Simpson's rule
    area = 0
    if (N+1)%2 == 0: #check that the number of points given are odd, as is required by Simpson's rule
        print("Simpson's Rule requires an array of odd length") 
        N = N - 1
    for i in range(1,N+1):
        if i == 1 or i == N+1:
            wsimp = h/3
            area = area + wsimp*F(i)
        elif i % 2 == 0:
            wsimp = 4/3*h
            area = area + wsimp*F(i)
        else:
            wsimp = 2/3*h
            area = area + wsimp*F(i)
    return area

            
print("Simpson's Rule Integral: ", simpo(N)) # Integration using Simpson's Rule

