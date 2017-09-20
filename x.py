# -*- coding: utf-8 -*- 
import numpy as np 
import matplotlib.pyplot as plt
x = np.linspace(-1, 1, 10000) 
y = (x**2/2+x+1)
z = (2.7**x)
     
plt.figure(figsize=(8,4)) 
plt.plot(x,y,color="red",linewidth=2) 
plt.plot(x,z,color="blue") 
plt.xlabel("Time(s)") 
plt.ylabel("Volt") 
plt.title("PyPlot First Example") 
plt.ylim(-1,3) 
plt.legend() 
plt.show() 