import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt
import re
import math

def process_input(file) :
 input_file = open(file)
 text = input_file.readlines()
 vectors_x = []
 for vectors in text :
 	v = vectors.split(' ')
 	if v[2] == '' :
 		x1 = re.search('(.*)\n',v[3])
 	else :
 	    x1 = re.search('(.*)\n',v[2])
 	x1 = float(x1.group())
 	x = np.array([[1.0],[x1]])
 	vectors_x.append(x)
 return vectors_x

def process_output(file) :
 input_file = open(file)
 text = input_file.readlines()
 vectors_x = []
 for vectors in text :
 	v = vectors.split(' ')
 	if v[2] == '' :
 		x1 = re.search('(.*)\n',v[3])
 	else :
 	    x1 = re.search('(.*)\n',v[2])
 	x1 = float(x1.group())
 	x = np.array([x1])
 	vectors_x.append(x)
 return vectors_x

def create_Y(input_vectors) :
 Y = np.array([0])
 for y in input_vectors :
  Y = np.vstack((Y,y))
 return Y  	
   
def create_X(input_vectors) :
 X = np.array([[0,0]])
 for vector in input_vectors :
  X = np.vstack((X,np.transpose(vector)))
 return X

def wlms(input,output,x,t):
  w = np.zeros((len(input),len(input)))
  for i in range(0,len(input)):
  	w[i][i] = math.exp(-math.pow((x-input[i][1])/t,2)) 
  b = np.dot(np.transpose(input),w)
  a = la.inv(np.dot(b,input))
  parameter = np.dot(a,b)
  parameter = np.dot(parameter,output)
  return parameter

xinput = input("Enter path for x-data\n")
yinput = input("Enter path for y-data\n")
inp = create_X(process_input(xinput))
out = create_Y(process_output(yinput))

x = []
for vect in inp :
	x.append(vect[1])
y = out
for i in range(-20,65):
	i /= 5.0
	ans = wlms(inp,out,i,5)
	x2 = np.array([j for j in range(int(i-1),int(i+1))])
	y2 = np.array([ans[0] + ans[1]*i for i in x2])
	plt.plot(x2,y2)

plt.scatter(x,y)
plt.xlim(-2,15)
plt.ylim(-1,3)
plt.show()

