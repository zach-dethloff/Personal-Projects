import numpy as np
import matplotlib.pyplot as plt

def wavefunc(E,r): # Function using the numerov method to determine the energy eigenvalues of a proton in a square well of depth 83MeV
    psi = np.zeros((2, 1000))
    psio = np.zeros((2, 1000))

    dl    = 1e-8                      # very small interval to stop bisection
    ul    = np.zeros(1501)
    ur    = np.zeros(1501)
    k2l   = np.zeros(1501)                        # k**2 left wavefunc
    k2r   = np.zeros(1501)                         
    n     = 1501
    nl    = n
    nr    = n
    m     = 5                                           # plot every 5 points
    imax  = 100 
    xl0   = -2*r   
    xr0   = 2*r
    h     = 1.0*(xr0-xl0)/(n-1.)  
    amin  = -0.01; amax  = -0.00085                            # root limits
    e     = E                                 # Initial E guess
    de    = 0.01
    ul[0] = 0.0; ul[1] = 0.00001; ur[0] = 0.0; ur[1] = 0.00001     
    xstep = np.linspace(xl0,xr0,n)
    im = int(0.75*n)  # match point
    istep=0

    def V(x):                                                   # Square well definition
        if (abs(x)<=r):
            v = -83                            
        else:
            v = 0
        return v

    def setk2():                                                       #  k2  
        for i in range(0,n):         
            xl = xl0+i*h
            xr = xr0-i*h
            k2l[i] = 0.0483*(e-V(xl))
            k2r[i] = 0.0483*(e-V(xr))

    def numerov (n,h,k2,u):                             # Numerov algorithm  
        b=(h**2)/12.0
        for i in range(1,n-1):  
            u[i+1] = (2*u[i]*(1-5*b*k2[i])-(1.+b*k2[i-1])*u[i-1])/(1+b*k2[i+1])

    setk2()
    numerov (nl, h, k2l, ul)                                       # Left psi
    numerov (nr, h, k2r, ur)                                       # Right psi
    fact= ur[nr-2]/ul[im]                                             # Scale
    # for i  in range (0,nl): ul[i] = fact*ul[i]
    # f0 = (ur[nr-1]+ul[nl-1]-ur[nr-3]-ul[nl-3])/(2*h*ur[nr-2])    #  Log deriv

    def normalize():    
        asum = 0
        for i in range( 0,n):                     
            if i > im :
                ul[i] = ur[n-i-1]
                asum = asum+ul[i]*ul[i]
        asum        = np.sqrt(h*asum); 
        j=0
        for i in range(0,n,m):                   
            xl        = xl0 + i*h
            ul[i]     = ul[i]/asum                 # wave function normalized
            psi[0][j]  = xl                                   # plot psi
            psi[1][j]  = ul[i]       # vertical line for match of wvfs
            psio[0][j] = xl 
            if e < -60:
                psio[1][j] = ul[i]**2/2
            elif e > -25:
                psio[1][j] = ul[i]**2*2
            else:
                psio[1][j] = ul[i]**2
            j += 1


    normalize()
    tpsi = psio[1][:150]
    t2psi = tpsi[::-1]
    psio[1][152:302] = t2psi

    plt.plot(psio[0][:301],psio[1][:301]+e,label='E = %d' % e) # plot of the allowed energies in the well
    plt.hlines(e,xl0,xr0,linestyle='--') # well shape
    well = []
    for val in xstep:
        well.append(V(val))
    plt.plot(xstep,well)
    plt.grid()

    
plt.figure(figsize=(10,6))   
E = [-75,-52,-18]
r = 2
for val in E:
    wavefunc(val,r)
    
plt.legend()
plt.title('Allowed energies in a potential well')


rs = [4,5,7] # finding the 1st energy eigenstate of wells of different well radii
for vals in rs:
    wavefunc(E[0],vals)
