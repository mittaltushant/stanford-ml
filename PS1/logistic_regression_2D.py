import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt
import re
import math 
from mpl_toolkits.mplot3d import Axes3D

file_x = input("Enter path for x-data\n")
file_y = input("Enter path for y-data\n")
init_p = np.array([[0.0,0.0,0.0]])

def process_x(file):
 input_file = open(file)
 text = input_file.readlines()
 vectors_x = []
 for vectors in text :
 	v = vectors.split(' ')
 	x1 = float(v[3])
 	if v[5] == '' :
 		x2 = re.search('(.*)\n',v[6])
 	else :
 	    x2 = re.search('(.*)\n',v[5])
 	x2 = float(x2.group())
 	x = np.array([[1.0],[x1],[x2]])
 	vectors_x.append(x)
 return vectors_x	
 
def process_y(file) :
  input_file = open(file)
  text = input_file.readlines()
  vectors_y = []
  for vectors in text :
 	v = vectors.split(' ')
 	y = np.array([[float(v[3])]])
 	vectors_y.append(y)
  return vectors_y

def log(x,y,init):
 final = init + (float(y) - h(x,init))*np.transpose(x)
 return final

def h(x,init):
 product = float(np.dot(init,x))
# print product
 h = 1.0/(1 + math.exp(-product))
 return h 

def plot ():
 positive = []
 negative = []
 x = []
 y = []
 for i in range(0,len(vx)) :
  if float(vy[i]) :
   x.append(np.array(float(vx[i][1])))
   y.append(np.array(float(vx[i][2])))
 plt.scatter(x,y)
 x = []
 y = []

 for i in range(0,len(vx)) :
  if float(vy[i]) == 0 :
   x.append(np.array(float(vx[i][1])))
   y.append(np.array(float(vx[i][2])))
 plt.scatter(x,y,marker='*')

 x2 = np.array([i for i in range(-5,10)])
 y2 = np.array([-init_p[0][0]/init_p[0][2] - (init_p[0][1]*i)/init_p[0][2] for i in x2])
 plt.plot(x2,y2)
 plt.show()

vx = process_x(file_x)
vy = process_y(file_y)
for i in range(1,50) : 
 hess = np.zeros((3,3))
 grad = np.zeros((3,1))
 for i in range(0,len(vx)):
  hess -= h(vx[i],init_p)*(1-h(vx[i],init_p))*np.dot(vx[i],np.transpose(vx[i]))
  grad += (float(vy[i])-h(vx[i],init_p))*vx[i]
 a = np.dot(np.transpose(np.dot(la.inv(hess),grad)),np.dot(la.inv(hess),grad))
 print a[0][0]
 if  a < 0.00000000000000001 :
  break
 else :
  init_p -= np.transpose(np.dot(la.inv(hess),grad))
 print init_p 

print init_p    		
plot()
