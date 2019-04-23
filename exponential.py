import matplotlib.pyplot as plt
import numpy as np
fs=10000
f1=1000
f2=200
t=np.arange(1,50,0.1)
x=np.exp(2*np.pi*t*f1/fs)
plt.subplot(2,1,1)
plt.plot(t,x)
plt.xlabel('samples')
plt.ylabel('amp')
plt.title('+ve exponetial wave')

y=np.exp(-2*np.pi*t*f1/fs)
plt.subplot(2,1,2)
plt.plot(t,y)
plt.xlabel('samples')
plt.ylabel('amp')
plt.title('-ve exponetial wave')
plt.show()
