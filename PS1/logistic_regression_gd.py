import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt
import re
import math 

file_x = input("Enter path for x-data\n")
file_y = input("Enter path for y-data\n")
init_p = np.array([[0,0,0]])

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
 product = float(np.dot(init,x))
 h = 1.0/(1 + math.exp(-product))
 final = init + (float(y) - h)*np.transpose(x)
 return final

vx = process_x(file_x)
vy = process_y(file_y)
for i in range(0,len(vx)):
 init_p = log(vx[i],vy[i],init_p)
print init_p   		