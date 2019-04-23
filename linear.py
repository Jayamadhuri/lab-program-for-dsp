import numpy as np
import cmath as c
import matplotlib.pyplot as plt
#j=c.sqrt(-1)
def dft(x1,N):
	k=np.arange(0,N)
	n1=np.arange(0,N)
	z=len(x1)
	if z<N:
		q=N-z
		x1=np.append(x1,np.zeros(q))
	y=[]
	M=[]
	P=[]
	for i in k:
		sum=0;
		for j in n1:
			sum+=x1[j]*np.exp(-1*2*np.pi*1j*i*j/np.float(N))
		y.append(sum)
		M.append(np.abs(sum))
		P.append(np.angle(sum))
	"""
	plt.subplot(311)
	plt.plot(k,x1)
	plt.subplot(312)
	plt.plot(k,M)
	plt.subplot(313)
	plt.plot(k,P)
	plt.show()
	"""
	return M

N=input("number of dft ponts")
x1=input("enter values1")#ex:a=[1,2,3]
#N1=input("number of dft points")
x2=input("enter values2")
if(len(x1)>len(x2)):
	q=len(x1)-len(x2)
	x2=np.append(x2,np.zeros(q))
else:
	q=len(x2)-len(x1)
	x2=np.append(x1,np.zeros(q))
q=len(x1)
x3=[]
a=0
for i in range(q):
	a=x1[i]+x2[i]
	x3.append(a)
M=dft(x3,N)
print(M)
P=dft(x1,N)
print(P)
U=dft(x2,N)
print(U)
b=0
X3=[]
for l in range(len(U)):
	b=P[l]+U[l]
	X3.append(b)
print(X3)
plt.subplot(211)
plt.plot(M)
plt.subplot(212)
plt.plot(X3)
plt.show()
#dft(x1,N)
