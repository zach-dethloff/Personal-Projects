import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate
import matplotlib.animation as animation

ra = [0,4] # intial points
rb = [-3,0]
rc = [0,0]
T = 10 # seconds
m_a = 3 # object masses
m_b = 4
m_c = 5
w = 2*np.pi/T # angular velocity
rab = 5**3 
rac = 4**3
rbc = 3**3


def derivs(state2, t): # function for determining the solutions of the equation of motion over time for each of these objects
    x_a = state2[0]
    y_a = state2[2]
    x_b = state2[4]
    y_b = state2[6]
    x_c = state2[8]
    y_c = state2[10]
    out = np.zeros_like(state2)

    d_ab_3 = d_ba_3 = ((x_a-x_b)**2+(y_a-y_b)**2)**(3/2) # equations of motion due to the forces acting on each of the bodies
    d_ac_3 = d_ca_3 = ((x_a-x_c)**2+(y_a-y_c)**2)**(3/2)
    d_bc_3 = d_cb_3 = ((x_b-x_c)**2+(y_b-y_c)**2)**(3/2)

    out[0] = state2[1]
    out[1] = -m_b*(x_a-x_b)/d_ab_3 - m_c*(x_a-x_c)/d_ac_3 # updating the lists to the new states of each of the objects
    out[2] = state2[3]
    out[3] = -m_b*(y_a-y_b)/d_ab_3 - m_c*(y_a-y_c)/d_ac_3
    out[4] = state2[5]
    out[5] = -m_a*(x_b-x_a)/d_ba_3 - m_c*(x_b-x_c)/d_bc_3
    out[6] = state2[7]
    out[7] = -m_a*(y_b-y_a)/d_ba_3 - m_c*(y_b-y_c)/d_bc_3
    out[8] = state2[9]
    out[9] = -m_a*(x_c-x_a)/d_ca_3 - m_b*(x_c-x_b)/d_cb_3
    out[10] = state2[11]
    out[11] = -m_a*(y_c-y_a)/d_ca_3 - m_b*(y_c-y_b)/d_cb_3
    return out


dt = 0.01 # time step
tint = np.arange(0,T,dt)
state = (0,0,4,0,-3,0,0,0,0,0,0,0) # starting state of the system

all_positions = integrate.odeint(derivs,state,tint) # finding all of the positions over time t = 0 to 10 seconds, using the derivs function described above

ax = all_positions[:,0]
ay = all_positions[:,2]

bx = all_positions[:,4]
by = all_positions[:,6]

cx = all_positions[:,8]
cy = all_positions[:,10]

plt.scatter(ax,ay,label='A') # plot of each of the positions over time
plt.scatter(bx,by,label='B',color='orange')
plt.scatter(cx,cy,label='C',color='green')
plt.title('Trajectories of Points A, B, C')
plt.xlabel('x - [m]')
plt.ylabel('y - [m]')
plt.legend()
plt.show() # we see the system spiral into chaos which is exactly what is expected for a 3-Body Problem

# Now I test a stable state of the 3-Body Problem, which can only exist under very specific conditions

m_a = 1 # all masses are the same
m_b = 1
m_c = 1


x = 0.97000436 # intial conditions, similar for all objects
y = -0.24308753

vx = -0.93240737
vy = -0.86473146

state2 = (x, -0.5*vx, y, -0.5*vy, -x, -0.5*vx, -y, -0.5*vy, 0, vx, 0, vy) # information for the new state

times = np.arange(0,10,0.001) # again observing the orbits over 10 seconds
output = integrate.odeint(derivs,state2,times) # finding the positions over time using the same previously defined function

ax = output[:,0] # Positions for bodies in this new state
ay = output[:,2]

bx = output[:,4]
by = output[:,6]

cx = output[:,8]
cy = output[:,10]

plt.figure()
plt.scatter(ax,ay)
plt.title('1st Bodies Motion')
plt.figure()
plt.scatter(bx,by,color='orange')
plt.title('2nd Bodies Motion')
plt.figure()
plt.scatter(cx,cy,color='g')
plt.title('3rd Bodies Motion') # 3 Figure 8 paths are recovered, which is expected since this state is named the "Figure-8 Orbit".

# The stability of this orbit is determined by slightly varying initial conditions

m_a = 1
m_b = 1
m_c = 1


x = 0.99
y = -0.26

vx = -0.91
vy = -0.84

state2 = (x, -0.5*vx, y, -0.5*vy, -x, -0.5*vx, -y, -0.5*vy, 0, vx, 0, vy)

times = np.arange(0,8*np.pi,0.001)
output = integrate.odeint(derivs,state2,times)

ax = output[:,0]
ay = output[:,2]

bx = output[:,4]
by = output[:,6]

cx = output[:,8]
cy = output[:,10]

plt.figure()
plt.scatter(ax,ay)
plt.title('1st Bodies Motion')
plt.figure()
plt.scatter(bx,by,color='orange')
plt.title('2nd Bodies Motion')
plt.figure()
plt.scatter(cx,cy,color='g')
plt.title('3rd Bodies Motion')
