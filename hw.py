import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9,10])
y = x
y_sqr=x**2
y_cub=x**3
plt.plot(x,y,color='red')
plt.plot(x,y_sqr,color='blue')
plt.plot(x,y_cub,color='green')
plt.axis([0,10,0,100])
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()