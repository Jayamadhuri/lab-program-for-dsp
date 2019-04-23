#To find the dtft of the given discrete signal
from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
x=[6,4,6,3,2,7]
N=1000
j=cm.sqrt(-1)
X=[]
w=np.linspace(-np.pi,np.pi,N)
for i in range(0,N):
        sum=0
        for n in range(0,len(x)):
            sum=sum+(x[n]*np.exp(-n*w[i]*j))
        X.append(sum)
plt.subplot(221)
plt.plot(w,np.abs(X))
plt.xlabel('freq(w/pi)')
plt.ylabel('magnitude')
plt.title('magnitude spectrum')
plt.grid()
plt.subplot(222)
plt.plot(w,angle(X)/np.pi)
plt.xlabel('freq(w/pi)')
plt.ylabel('phase angle in radian')
plt.title('phase spectrum')
plt.grid()
plt.show()
    