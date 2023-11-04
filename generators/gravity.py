# simulate measurements of free falling objects

import numpy as np
import os

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

g = 9.81
h = 1


t_final = np.sqrt((0 - h) / (-1.0 / 2.0 * g))

print("tfinal: ", t_final)

# evaluate exact position z(t) with n measurements
n = 12
t = np.linspace(0, t_final, n)
z0 = h
z = z0 - 1 / 2 * g * t**2
# measured height and t are affected by nrmal distributed errors f mean zero and sizes:
z_error = 0.05
t_error = 0.01
z_measured = z + np.random.normal(0, z_error)
t_measured = t + np.random.normal(0, t_error)

with open(script_dir+"/../csv/gravity.csv", "w") as fh:
    print("time,height",file=fh)
    for i in range(len(t)):
        print(f"{t_measured[i]:.1f},{z_measured[i]:.2f}", file=fh)

# plot to check
import matplotlib.pyplot as plt

plt.plot(np.round(t_measured, 1), np.round(z_measured, 2), "o-")
plt.show()
