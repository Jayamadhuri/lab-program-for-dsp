mport numpy as np
import matplotlib.pyplot as plt
def dtft(x):
	y=[ ]
	w=np.arange(-1.0*np.pi,np.pi,np.pi/500)
	for i in w:
		sum=0
		for n in range(len(x)):
			if n>=0 and n<len(x):
				k=complex(0,-1)
				sum=sum+(x[n]*np.exp(k*i*n))
		y=np.append(y,sum)
	return(y)



m=int(input("Enter length"))
x=[ ]
for j in range(m):
	t=int(input("Enter samples:"))
	x=np.append(x,t)
print(x)
print ("DTFT=",dtft(x))

w=np.arange(-1.0*np.pi,np.pi,np.pi/500.0)
f1=int(input("enter signal frequency"))
fs=int(input("enter sampling frequency"))
r=np.arange(-200,200,1)
y1=np.cos(2*np.pi*float(f1)/float(fs)*r)
plt.subplot(3,1,1)
plt.plot(y1)
plt.title('Input Signal')
plt.subplot(3,1,2)
plt.plot(w,np.abs(dtft(y1)))
plt.title('Magnitude of rhe Signal')
plt.subplot(3,1,3)
plt.plot(w,np.angle(dtft(y1)))
plt.title('phase of rhe Signal')
plt.show( )