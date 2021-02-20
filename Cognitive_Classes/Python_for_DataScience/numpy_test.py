import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-2*np.pi,2*np.pi,10000)
y=np.sin(x)
plt.plot(x,y)
plt.show()

sig=1/(1+np.exp(-x))
plt.plot(x,sig)
plt.show()


z=np.cos(x)
plt.plot(x,z)
plt.show()