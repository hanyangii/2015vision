import numpy as np
import matplotlib.pyplot as plt
import math
import random
from numpy import*
from scipy.linalg import *
from scipy.cluster.vq import *

from kmeans import *

Points=[]

class datas:
	def __init__(self,d):
		self.var=[[] for x in range(d+1)]
	def append_var(self, i, val):
		self.var[i].append(val)

def affinity(data_,k,d):
	Points_num=0
	for i in range(len(data_)):
		Points_num+=1
		coords=[]
		for j in range(d):
			coords.append(data_[i][j])

		point=Point(coords,None)
		Points.append(point)

	W = np.zeros((Points_num, Points_num))
	sigma=1
	for i in range(Points_num):
		for j in range(i+1, Points_num):
			x=Points[i]
			y=Points[j]
			similarity = np.exp(-1*getDistance(x,y,d)**2/2*(sigma**2))
			W[i][j]=similarity
			#print j
		#print i
	
	#print W
	return W

def spectral(L,k):
	e_val, e_vec = eig(L)
	
	#print e_val
	#print e_vec
	
	idx=e_val.argsort()
	e_val.sort()
	e_vec_sort=e_vec[:, idx]
	e_vec=e_vec_sort
	
	dat = datas(k)

	for t in range(len(e_vec)):
		for j in range(k):
			dat.append_var(j, float(e_vec[t][j]))
		

	label=k_means_clustering_(dat, k, k)
	#print len(e_vec), len(label)
	
	if not len(Points[0].coords)==2 and k<16:
		return label 

	t_=0
	colors=["pink", "purple", "black", "yellow", "green", "blue", "red", "navy", "ivory", "gray", "yellowgreen", "skyblue", "brown", "violet", "orange"]
	for k in Points:
		#print k.coords[0], k.coords[1],label[t_]
		plt.plot(k.coords[0],k.coords[1],'o',markersize=5, color=colors[label[t_]],alpha=1)
		t_+=1
	
	plt.legend()
	plt.show()
	
	print label
	return label



def spectral_clustering_(W, k):
	D = np.diag([sum(t) for t in W])
	#print D
	L=D-W
	return spectral(L,k)
	

