import numpy as np
import matplotlib.pyplot as plt
m=31
t=np.arange(0,m,1)
p=[]
for n in range(0,m):
	w=np.cos((2*np.pi*n)/(m-1))
	x=0.5*w
	y=np.cos((4*np.pi*n)/(m-1))
	z=0.08*y
	q=0.42-x+z
	p=np.append(p,q)
plt.stem(t,p)
plt.show()

