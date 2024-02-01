import numpy as np
import matplotlib.pyplot as plt

# Demonstration of an n-point Lagrange interpolation using experimental neutron scattering data and fitting polynomial function from Computational Physics: Problem Solving with Python, Third Edition (Wiley-VCH, 2015), by Rubin Landau, Manuel Páez, and Cristian Bordeianu

def npL(f, xk): # N-point Lagrange interpolation function 
 
    result = 0.0 # iteritavely updated value which returns the next point in the fit
    n = len(f)
    for i in range(n):
 
        term = f[i][1] # scans through test values
        for j in range(n):
            if j != i: # ensuring the data doesn't come from the same pair
                term = term * (xk - f[j][0]) / (f[i][0] - f[j][0]) # interpolation equation using test-values
 
        result += term
 
    return result
 

f = [[0, 10.6], [25, 16], [50, 45], [75, 83.5], [100,52.8], [125,19.9], 
     [150,10.8], [175,8.25], [200,4.7]] # test points
 

x = np.arange(0,201,1)
pts = []
for val in x:
    pts.append(npL(f,val))
    
print(pts)

plt.plot(x,pts,label='Interpolated Function')
for val in f:
    plt.scatter(val[0],val[1],color='k',label='Known Point: %d,%d' %(val[0],val[1])) # Overlaying known points on to the fitted function
    
plt.legend()

ep = pts.index(max(pts))
print("Estimated peak position at %d,%d" %(x[ep],max(pts))) # Finding the coordinates of the peak of this function

hm = []
pk = max(pts)/2
pv = pts[35:125]
xv = x[35:125]

for val in pv:
    hm.append(abs(max(pv)/2-val))
    
l1 = xv[hm.index(min(hm))] # routine to find the full-width at half-maximum value
del hm[hm.index(min(hm))]
l2 = xv[hm.index(min(hm))]
fwhm = l2-l1
print("width of curve at half maximum %d" % fwhm)
