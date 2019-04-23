import matplotlib.pyplot as plt
import numpy as np
fs=10000
f1=1000
f2=200
t=np.arange(-50,50,0.1)
x=np.sinc(2*np.pi*t*f1/fs)
plt.plot(t,x)
plt.xlabel('samples')
plt.ylabel('amp')
plt.title('sinc wave')
plt.show()
