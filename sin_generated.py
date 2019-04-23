import matplotlib.pyplot as plt
import numpy as np
fs=10000
f1=1000
f2=500
t=np.arange(1,50,0.1)
x=np.sin(2*np.pi*t*f1/fs)
plt.plot(t,x)
plt.xlabel('samples')
plt.ylabel('amp')
plt.title('sin wave-1')
plt.show()
