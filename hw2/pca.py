import numpy as np
import string
import matplotlib.pyplot as plt
import math

def pca_(data, d):
	Points=[]
	for i in range(len(data.var[0])):
		coords=[]
		for j in range(d):
			coords.append(data.var[j][i])
		Points.append(coords)
	
	mean=[]
	mean_val=[]
	dat=[]
	for i in range(d):
		mean_val.append(np.mean(data.var[i]))
	
	for i in range(len(Points)):
		x=[]
		for j in range(d):
			x.append(Points[i][j]-mean_val[j])
		mean.append(x)
	
	#print 'sssssssssssssssssssssssssssssssssssssssssssssssssssssss'
	#print mean, np.transpose(mean)	
	scatter = np.dot(np.transpose(mean),mean)
	eig_val_sc, eig_vec_sc = np.linalg.eig(scatter)
	
	print eig_vec_sc
	return eig_val_sc
