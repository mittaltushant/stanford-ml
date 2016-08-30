from scipy import misc
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
img_matrix = misc.imread('bird_small.tiff')
img_copy = img_matrix
clusters = []
point_list = []
img_list = []

def make_list(clusters):
	point_list =[]
	for vectors in clusters:
		point_list.append([vectors])
	return point_list	


def init_clusters():
	global point_list
	global img_list
	for i in range(0,16):
		rand_point = [random.randint(0,127),random.randint(0,127)]
		vector = np.array(img_matrix[random.randint(0,127),random.randint(0,127)])
		clusters.append(vector)
		img_list.append([rand_point])
	point_list = make_list(clusters)
	return

def assign_clusters():
	global point_list
	global img_list
	for i in range(0,16):
		img_list[i] = [img_list[i][0]]
	for i in range(127,-1,-1):
		for j in range (0,128):
			min_d = np.dot(img_matrix[i,j]-clusters[0],img_matrix[i,j]-clusters[0])			
			cluster_num = 0
			for k in range(1,16):
				d = np.dot(img_matrix[i,j]-clusters[k],img_matrix[i,j]-clusters[k])
				if d<min_d :
					min_d = d
					cluster_num = k
			point_list[cluster_num].append(img_matrix[i,j])
			img_list[cluster_num].append([i,j])
	return	


def center_clusters():
	global clusters
	global point_list
	global img_list
	for i in range(0,16):
		total = np.array([0,0,0])
		for vectors in point_list[i]:
			total += vectors
		total /= len(img_list[i])
		clusters[i] = total
			
init_clusters()

for i in range(0,50):
	assign_clusters()
	center_clusters()
	'''fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	for j in range (0,16):
		for vect in point_list[j]:
			xs = vect[0]
			ys = vect[1]
			zs = vect[2]
			ax.scatter(xs, ys, zs, c=(clusters[j][0]/255.0,clusters[j][1]/255.0,clusters[j][2]/255.0))
	ax.set_xlabel('X Label')
	ax.set_ylabel('Y Label')
	ax.set_zlabel('Z Label')
	plt.show()'''

	point_list = make_list(clusters)
	

for i in range (0,16):	
	for point in img_list[i]:
		img_copy[point[0],point[1],0] = clusters[i][0]
		img_copy[point[0],point[1],1] = clusters[i][1]
		img_copy[point[0],point[1],2] = clusters[i][2]

plt.imshow(img_copy)
plt.show()