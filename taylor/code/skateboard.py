import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

# 1.51
# initial conditions
phi0 = np.pi / 2
dot_phi0 = 0

# constants
R = 5 # [m]
g = 9.8 # [m/s^2]

# differential equation
def ddot_phi(phi, t):
    return [phi[1], -g / R * np.sin(phi[0])]

# time
t = np.linspace(0, 10, 1000)

# solve the differential equation
pos, vel = sp.integrate.odeint(ddot_phi, [phi0, dot_phi0], t).T

# approximate solution
omega = np.sqrt(g / R)
pos_approx = phi0 * np.cos(omega * t)

# plot the solution
plt.plot(t, pos)

# plot the approximate solution
plt.plot(t, pos_approx, '--')

plt.xlabel('t [s]')
plt.ylabel('$\phi$ [rad]')

# create legend
plt.legend(['$\phi(t)$', '$\phi_{approx}(t)$'])
plt.show()