import numpy as np
import matplotlib.pyplot as plt
def dft(x):
	y=[ ]
	
	if len(x)<N:
		x=np.append(x,np.zeros(N-len(x)))

	for k in range (0,N):
		sum=0
		for n in range (0,N):
			if n>=0 and n<len(x):
				t=complex(0,-1)
				sum=sum+ (x[n]*np.exp((t*2*np.pi*k*n)/float(N)))
		y=np.append(y,sum)
	return(y)


s=int(input("Enter No. of Samples:"))
x=[ ]
for i in range(s):
	s1=int(input("Enter:"))
	x=np.append(x,s1)
print(x)
N=int(input("Enter no. of DFTS:"))
print(dft(x))

f=int(input("Enter signal frequency:"))
fs=int(input("Enter Sampling frequency:"))
x1=np.arange(-200,200,1)
y1=np.sin(2*np.pi*(float(f)/float(fs))*x1)
k=np.arange(0,N)
y2=np.abs(dft(y1))
y3=np.angle(dft(y1))
plt.subplot(311)
plt.plot(x1,y1)
plt.title('Signal')
plt.subplot(312)
plt.plot(k,y2)
plt.title('Magnitude')
plt.subplot(313)
plt.plot(k,y3)
plt.title('Phase')
plt.show()
