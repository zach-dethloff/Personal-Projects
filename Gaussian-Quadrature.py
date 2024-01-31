import numpy as np
import matplotlib.pyplot as plt

# This is a demonstration of the use of Gaussian Quadrature to evalute an integral containing two functions, one of them being a weighting function, and the other an exponential. This evaluation will be done with the aid of a table, whose values are just below.

w2 = 0.8862269 # Given values of the weighting function based on the number of terms in the sum used to approximate the integral. The number following each of the letters indicates how many terms are being used
x2 = [0.7071068, -0.7071068] # zeros of the function, also based on the number of terms in the sum
w3 = [0.2954090, 1.1816359, 0.2954090]
x3 = [1.2247449, 0, -1.2247449]
w4 = [0.0813128, 0.8049141, 0.8049141, 0.0813128]
x4 = [1.6506801, 0.5246476, -0.5246476, -1.6506801]

sum22 = 0 # each of the values of the function after integration via Gaussian Quadrature
sum24 = 0
sum26 = 0

sum32 = 0
sum34 = 0
sum36 = 0

sum42 = 0
sum44 = 0
sum46 = 0

def G2(x): # Different exponents of the variable of integration, x
    return x**2

def G4(x):
    return x**4

def G6(x):
    return x**6


for i in range(0,2): # the number of iterations is equal to the number of terms used in the approximation sum
    sum22 = sum22 + w2*G2(x2[i])
    sum24 = sum24 + w2*G4(x2[i])
    sum26 = sum26 + w2*G6(x2[i])
    
for i in range(0,3):
    sum32 = sum32 + w3[i]*G2(x3[i])
    sum34 = sum34 + w3[i]*G4(x3[i])
    sum36 = sum36 + w3[i]*G6(x3[i])
    
for i in range(0,4):
    sum42 = sum42 + w4[i]*G2(x4[i])
    sum44 = sum44 + w4[i]*G4(x4[i])
    sum46 = sum46 + w4[i]*G6(x4[i])
    
print("The exact integral of the term containing x^2 is: ", np.sqrt(np.pi)/2)
print("The exact integral of the term containing x^4 is: ", 3*np.sqrt(np.pi)/4)
print("The exact integral of the term containing x^6 is: ", 15*np.sqrt(np.pi)/8)
print(sum22, sum24, sum26)
print(sum32, sum34, sum36)
print(sum42, sum44, sum46)
# Here we can see the that using two terms in the sum only returns a valid answer for the x^2 integration, not x^4 and x^6
# Increasing our iterations increases the accuracy of the result, and therefor by N=4 (N being the number of terms in the sum), our integration method is precise enough to effectively approximate x^6

def b(x): # Testing out the method of gaussian quadrature on a different exponential function
    return 1/(np.exp(x) + 1)

sumb = 0

for i in range(0,4):
    sumb = sumb + w4[i]*b(x4[i])

sumb
