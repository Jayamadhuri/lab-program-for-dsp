

import numpy as np
import matplotlib.pyplot as plt
def convolve(x,h):

	y=[]
	b=(len(x)+len(h)-1)

	for n in range(b):
		sum=0
		for k in range(len(x)):
			if n-k<len(h) and n-k>=0:
				sum=sum+(x[k]*h[n-k])
		y=np.append(y,sum)		
	return (y)
def timerev(x):
	lnx=len(x)
	y=np.zeros(lnx)
	for i in range(lnx):
		if lnx-i>=0 and lnx-i<=lnx:
			y[i]=x[lnx-i-1]
	return(y)
			
m=int(input("Enter samples:"))
x=[ ]
for i in range (m):
	y=int(input("Enter:"))
	x=np.append(x,y)
print (x)

p=int(input("Enter samples:"))
h=np.zeros(p)
for i in range(p):
	h[i]=int(input("Enter:"))
print (h)
result=convolve(x,h)
print("Convolution of two signals",result)

f=timerev(result)
print("Time reversal of Convolution", f)
rxy=convolve(x,f)
print("Cross Correlation",rxy)

f1=int(input("enter signal1 frequency:"))
f2=int(input("enter signal2 frequency:"))

fs=int(input("enter samplingfrequency:"))
x1=np.arange(0,100,0.1)
y1=np.sin(2*np.pi*(float(f1)/float(fs))*x1)
y2=np.sin(2*np.pi*(float(f2)/float(fs))*x1)

r=convolve(y1,y2)
q=timerev(r)
y3=convolve(y1,q)
N=np.random.rand(y1.shape[0])
xN=y1+N
h=[1.0/3.0,1.0/3.0,1.0/3.0]
y4=convolve(h,xN)
v=timerev(xN)
ac=convolve(v,xN)

plt.subplot(321)
plt.plot(y1)
plt.title('signal1')
plt.subplot(322)
plt.plot(y2)
plt.title('signal2')
plt.subplot(323)
plt.plot(r)
plt.title('Convolution of signal1 and signal2')
plt.subplot(324)
plt.plot(y3)
plt.title('Cross correlation ')
plt.subplot(325)
plt.plot(y4)
plt.title("Convolution of impulse response of MA system & xN")
plt.subplot(326)
plt.plot(ac)
plt.title('Auto correlation')



plt.show()


#Inputs:

#enter signal1 frequency:200
#enter signal2 frequency:400
#enter samplingfrequency:1000
