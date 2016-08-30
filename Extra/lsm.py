import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt
import random

def process_input() :
 points =[]
 for i in range (1,50) :
  x = random.randint(1,50) * random.random()
  points.append(np.array([1,x])) 
 return points

def process_output() :
  pass 

def create_Y() :
 Y = np.array([0])
 for i in range (1,50) :
  y = np.array([random.randint(1,50) * random.random()])
  Y = np.vstack((Y,y))
 return Y  	
   
def create_X(input_vectors) :
 X = np.array([0,0])
 for vector in input_vectors :
  X = np.vstack((X,vector))
 return X

def lms(input,output):
  parameter = np.dot(la.pinv(input),output)
  return parameter
  

inp = create_X(process_input())
out = create_Y()
ans = lms(inp,out)

x = []
for vect in inp :
	x.append(vect[1])

y = create_Y()
x2 = np.array([i for i in range(0,50)])
y2 = np.array([ans[0] + ans[1]*i for i in x2])


plt.scatter(x,y)
plt.plot(x2,y2)
plt.xlim(0,50)
plt.ylim(0,50)
plt.show()

