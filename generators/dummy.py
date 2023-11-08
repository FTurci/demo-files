# simulate measurements of free falling objects

import numpy as np
import os

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

t = np.linspace(0,10)
# x = np.sin(2*np.pi*t/3)+np.random.uniform(-0.1,0.1,len(t))
x =  t**3-4*t**2+t+np.random.uniform(-8,8,len(t))

np.savetxt("../csv/poly.csv",list(zip(t,x)),header="t,x",delimiter=",",comments="")