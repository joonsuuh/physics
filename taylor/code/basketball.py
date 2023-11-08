import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

# initial conditions
v_xo = 15 * np.sin(np.pi/4)
v_yo = v_xo
x_o = 0
y_o = 2

# constants
gamma = 0.25
g = 9.8
m = 0.6
D = 0.24
c = gamma * D ** 2
v_t = np.sqrt(m*g/c)

# time
t = np.linspace(0, 10, 1000)

# differential equations
def soe(t, s):
    x = s[0]
    y = s[1]
    v_x = s[2]
    v_y = s[3]
    dxdt = v_x
    dydt = v_y
    dv_xdt = -c/m * v_x * np.sqrt(v_x**2 + v_y**2)
    dv_ydt = -g - c/m * v_y * np.sqrt(v_x**2 + v_y**2)
    return [dxdt, dydt, dv_xdt, dv_ydt]

# solveing the differential equations
sol = sp.integrate.solve_ivp(soe, [0, 10], [x_o, y_o, v_xo, v_yo], t_eval=t)

# equation of motion in a vacuum
x_vac = v_xo * t
y_vac = y_o + v_yo * t - 0.5 * g * t**2

# plot the results
plt.plot(sol.y[0], sol.y[1])
plt.plot(x_vac, y_vac, 'r--') # solution in a vacuum
plt.ylim(0, 8)
plt.xlim(0, 25)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend(['quadratic drag', 'vacuum'])
plt.show()

# calculate the range when y = 0
# find the index of the first value of y that is less than zero
idx = np.where(sol.y[1] < 0)[0][0]

# calculate the range
range = sol.y[0][idx]
print("range = ", range)

# another way to calculate the range
it = np.nditer(sol.y[1], flags=['f_index']) 
for i in it:
    if i < 0:
        # print("range = ", sol.y[0][it.index])
        break

# range in a vacuum
index = np.where(y_vac < 0)[0][0]
range_vac = x_vac[index]
print("range_vac = ", range_vac)