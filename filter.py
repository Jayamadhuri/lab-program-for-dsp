import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
wr=[]
m=input("enter no.of samples:")
for n in range(0,m):
	wr=np.append(wr,1)
plt.stem(wr)
plt.show()
h=[]
fc=np.pi/4
n=np.linspace(-100,100,200)
print n
h=np.append(h,((np.sin(fc*n))/(np.pi*n)))
plt.stem(n,h)
plt.show()

def dtft(x):
	j=cm.sqrt(-1)
	y=[ ]
	N=100
	n=len(x)
	p=np.linspace(-np.pi,np.pi,N)
	for i in range(0,N):
		w=p[i]
		sum=0
		for k in range(0,n):
			sum=sum+x[k]*np.exp(-j*w*k)
		y.append(abs(sum))
	return y
y=dtft(h)
plt.stem(np.abs(y))
plt.show()
