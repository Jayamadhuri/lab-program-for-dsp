import matplotlib.pyplot as plt
import numpy as np
a=int(input("enter no.of rows="))
b=int(input("enter no.of columns="))
m=[]
for i in range(a):
	l=[]
	for j in range(b):
		l=np.append(int(input()))
	m.np.append(l)
print(m)
y=np.linalg.inv(m)
print("inverse of a matriX iS",y);
