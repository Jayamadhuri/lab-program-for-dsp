import numpy as np
import matplotlib.pyplot as plot
def movingavg(x):
	n=len(x)
	p=int(input("enter order:"))
	z= [ ]
	for i in range(n):
		sum=0
		for k in range(p):
			if (i-k<n) and (i-k>=0):
				s=sum+x[i-k]
				sum=s
		y=float(sum)/float(p)
		z=np.append(z,y)
	return (z)

n=int(input("enter sample length"))
x=np.zeros(n)
for i in range(n):
	x[i]=int(input("enter"))
print (x)
result1=movingavg(x)
print("moving average of a system:",result1)
f1=input(" frequency for 1st signal") 
#f2=input(" frequency for 2nd signal")
fs=input("enter your sampling frequency")
x=np.arange(0,100)
y1=np.sin(2*np.pi*x*(float(f1)/float(fs)))
#y2=np.sin(2*np.pi*x*(float(f2)/float(fs)))
y2=np.random.rand(y1.shape[0])
x=y1+y2
result2=movingavg(x)
plot.subplot(4,1,1)
plot.plot(y1)
plot.subplot(4,1,2)
plot.plot(y2)
plot.subplot(4,1,3)
plot.plot(x)
plot.subplot(4,1,4)
plot.plot(result2)
plot.xlabel('sample')
plot.ylabel('amplitude')
plot.show( )

#inputs:
#frequency for 1st signal30
#enter your sampling frequency500
#enter order:100





