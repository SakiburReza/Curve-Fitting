# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 18:35:14 2019

@author: Sakibur Reza
"""
import numpy as np
import matplotlib.pyplot as plt

file=open("data.txt",'r')
lines=file.readlines()
file.seek(0)
num_lines= sum(1 for line in file)
print("Number of Lines:",num_lines)
print()

x_sum=0
x2_sum=0
x3_sum=0
x4_sum=0
x5_sum=0
x6_sum=0
y_sum=0
xy_sum=0
x2y_sum=0
x3y_sum=0

X=[None]*num_lines
Y=[None]*num_lines

for i in range(num_lines):
    x= float(lines[i].split(" ")[0])
    y= float(lines[i].split(" ")[1])
    X[i]=x
    Y[i]=y
    x_sum+= x
    y_sum+=y
    x2_sum+= x**2
    x3_sum+=x**3
    x4_sum+=x**4
    x5_sum+=x**5
    x6_sum+=x**6
    xy_sum+=x*y
    x2y_sum+=x**2*y
    x3y_sum+=x**3*y

    
avg_y=y_sum/num_lines
plt.figure(figsize=(11,10))
plt.scatter(X,Y)

St=0
Sr=0
for i in range(num_lines):
    St+=(Y[i]-avg_y)**2

#For a first order curve
A=np.array([[num_lines,x_sum],[x_sum,x2_sum]])
B=np.array([y_sum,xy_sum])

C=np.linalg.solve(A,B)
f=np.arange(0,10,0.1)
f1=C[1]*f+C[0]
plt.plot(f,f1,'r',label="1st Order",linewidth=3)
for i in range(num_lines):
    Sr+=(Y[i]-C[1]*X[i]-C[0])**2
    

r=pow((St-Sr)/St,1/2)
print("For the first order curve:")
print("a0=",C[0]," a1= ",C[1])
print("Corelation Coefficient, r= ",r)
print();
#plt.show()

#For a second order curve
Sr=0
A=np.array([[num_lines,x_sum,x2_sum],[x_sum,x2_sum,x3_sum],[x2_sum,x3_sum,x4_sum]])
B=np.array([y_sum,xy_sum,x2y_sum])
C=np.linalg.solve(A,B)

f=np.arange(0,10,0.001)
f1=C[2]*f**2+C[1]*f+C[0]
plt.plot(f,f1,'g',label="2nd Order",linewidth=3)

for i in range(num_lines):
    Sr+=(Y[i]-C[2]*X[i]**2-C[1]*X[i]-C[0])**2
r=pow((St-Sr)/St,1/2)
print("For the second order curve:")
print("a0=",C[0]," a1= ",C[1]," a2= ",C[2])
print("Corelation Coefficient, r= ",r)
print()


#plt.show()


#For a third order curve
Sr=0
A=np.array([[num_lines,x_sum,x2_sum,x3_sum],[x_sum,x2_sum,x3_sum,x4_sum],[x2_sum,x3_sum,x4_sum,x5_sum],[x3_sum,x4_sum,x5_sum,x6_sum]])
B=np.array([y_sum,xy_sum,x2y_sum,x3y_sum])
C=np.linalg.solve(A,B)
f=np.arange(0,10,0.1)
f1=C[3]*f**3+C[2]*f**2+C[1]*f+C[0]
plt.plot(f,f1,'c',label="3rd Order",linewidth=3)

for i in range(num_lines):
    Sr+=(Y[i]-C[3]*X[i]**3-C[2]*X[i]**2-C[1]*X[i]-C[0])**2
r=pow((St-Sr)/St,1/2)
print("For the third order curve:")
print("a0=",C[0]," a1= ",C[1]," a2= ",C[2], " a3= ",C[3])
print("Corelation Coefficient, r= ",r)
plt.title("Curve Fitting")
plt.xlabel("Value of x")
plt.ylabel("Value of y")
plt.legend()
plt.grid()
plt.show()

