import numpy as np
import matplotlib.pyplot as plt
import random
import sys
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
positive = []
negative = []

weight_vector = np.array([1])
allvectors = []

def init_weight(n):
 global weight_vector
 #weight_vector = np.array(np.ones(n,dtype=float))
 weight_vector = np.array([0,0,0])

def get_vectors(file):
 f = open(file)
 text = f.readlines()
 for line in text :
  line = line.split(' \t')
  line = line[:-1]
  line_new = []
  for x in line :
   line_new.append(float(x)) 
  allvectors.append(np.array(line_new[:-1]))
  if line_new[-1] :
   positive.append(np.array(line_new[:-1]))
  else :
   negative.append(np.array(line_new[:-1]))

def correct(vector) :
 global weight_vector
 if any((vector == x).all() for x in positive) :
 	weight_vector += vector
 	
 else :
    weight_vector -= vector
    
def test(random_vector):
 global weight_vector
 #random_vector = allvectors[random.randint(0,3)]
 a = np.dot(random_vector,weight_vector)
 if (a<=0) and any((random_vector == x).all() for x in positive) :
  correct(random_vector)
 if (a>=0) and any((random_vector == x).all() for x in negative) :
  correct(random_vector)	
 

def isright() :
 for vectors in allvectors:
  a = np.dot(vectors,weight_vector)
  if (a<=0) and any((vectors == x).all() for x in positive):
   return False
  if (a>=0) and any((vectors == x).all() for x in negative) :
   return False
 return True

def plot() :
 x = np.array([0])
 y = np.array([0])
 z = np.array([0])
 for vectors in allvectors :
  x = np.append(x,float(vectors[1]))
  y = np.append(y,vectors[0])
  z = np.append(z,vectors[2])
 point = np.array([0,0,0])
 normal = weight_vector
 xx, yy = np.meshgrid(range(10), range(10))
 z1 =  (-normal[0]*xx - normal[1]*yy )*1./normal[2]
 Axes3D.scatter(ax,x,y,z)
 ax.plot_surface(xx,yy,z1, color='green')
 plt.show() 

file = '/home/tushant/Documents/CSE/Machine Learning/Codes/per_data'
init_weight(3)
get_vectors(file)
while True :
	for vectors in allvectors:
		test(vectors)
	if isright() :
		break
	print weight_vector	
print weight_vector

