import matplotlib.pyplot as boy;
import numpy as np;

f1=100
f2=100
fs=2000
n=100;
a=int(input("enter the phase of the wave"))
x1=np.arange(n)
y1=np.cos((2*np.pi*x1*f1/fs)+a)
boy.subplot(3,1,1)
boy.plot(x1,y1)
boy.xlabel("time")
boy.ylabel("amplitude")
boy.title("first wave") 

b=int(input("enter the phase of the second wave"))
y2=np.sin((2*np.pi*x1*f2/fs)+b) 
boy.subplot(3,1,2)
boy.plot(x1,y2)
boy.xlabel("time")
boy.ylabel("amplitude")
boy.title("second wave")

q2=y1+y2
boy.subplot(3,1,3)
boy.plot(x1,q2)
boy.xlabel("time")
boy.ylabel("amplitude")
boy.title("resulatnt wave")
boy.show()
 
