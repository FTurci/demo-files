# simulate measurements of free falling objects

import numpy as np
import os

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

x = np.linspace(0,10)
# x = np.sin(2*np.pi*t/3)+np.random.uniform(-0.1,0.1,len(t))
U =  0.5*x**3-4*x**2+x+np.random.uniform(-8,9,len(x))

np.savetxt("../csv/poly.csv",list(zip(x,U)),header="x,U",delimiter=",",comments="")
import matplotlib.pyplot as plt

plt.plot(x,U)
plt.show()