"""Dynamic Linear Equation Plotter
Task:
Ask the user to enter values for m and c

Plot the line y = mx + c for x values from -20 to 20

Add:

X and Y axis lines

Grid

Legend showing the equation"""

import matplotlib.pyplot as plt
import numpy as np

m=float(input("Input M: "))
c=float(input("Input C: "))
x=np.arange(-20,21,1)
y=x*m+c
plt.plot(x,y,color='red',label=f'y = {m}x + {c}')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.axhline(0,color='black',linewidth=0.5)
plt.axvline(0,color='black',linewidth=0.5)
plt.grid()
plt.legend()
plt.show()