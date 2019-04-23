 import numpy as np
import matplotlib.pyplot as plot
def conv(x,h):
	m=len(x)
	p=len(h)
	y=[ ]
	b=m+p-1
	for n in range(b):
		sum=0
		for k in range(m):
			if (n-k<p) and (n-k>=0):
				sum=sum+(x[k]*h[n-k])
		y=np.append(y,sum)
	return (y)

def timereverse(x):
	m=len(x)
	z=[ ]
	for i in range(m,0,-1):
		z=np.append(z,x[i-1])
	return z

m=int(input("enter samplesfor x"))
p=int(input("enter samples for h")) 
x=np.zeros(m)
for i in range(m):
	x[i]=int(input("enter"))
print (x)
h=np.zeros(p)
for i in range(p):
	h[i]=int(input("enter"))
print (h)
result1=conv(x,h)
print("rev=",timereverse(result1))
print ("convolution of two signals=",result1)

f1=input(" frequency for 1st signal") 
f2=input(" frequency for 2nd signal")
fs=input("enter your sampling frequency")
t=np.arange(0,10,0.1)
x1=np.sin(2*np.pi*t*(float(f1)/float(fs)))
h1=np.sin(2*np.pi*t*(float(f2)/float(fs)))
N=np.random.rand(x1.shape[0])
x_N=x1+N
h=[1.0/3.0,1.0/3.0,1.0/3.0]
y1=conv(x1,h1)
y2=conv(x1,timereverse(y1))
y3=conv(h,x_N)
y4=conv(x_N,timereverse(x_N))

plot.subplot(4,2,1)
plot.plot(x1)
plot.title('1st signal')

plot.subplot(4,2,2)
plot.plot(h1)
plot.title('2nd signal')

plot.subplot(4,2,3)
plot.plot(N)
plot.title('noise')

plot.subplot(4,2,4)
plot.plot(x_N)
plot.title('add noise to 1st signal')

plot.subplot(4,2,5)
plot.plot(y1)
plot.title('convolution(1st&2ndsignal)')

plot.subplot(4,2,6)
plot.plot(y2)
plot.title('CCF of 1st & 3rd signal reversal')

plot.subplot(4,2,7)
plot.plot(y3)
plot.title('convolution of 2nd & add(noise&1st)')

plot.subplot(4,2,8)
plot.plot(y4)
plot.title('ACF of (noise&1st)& its reversal')


plot.xlabel('sample')
plot.ylabel('amplitude')
plot.show( )

