import numpy as np
import math

def sum_W(cluster, mean_val,d):
	total=np.zeros((d,d))
	for i in cluster:
		x=[]
		for j in range(d):
			#print cluster[j], mean_val[j]
			x.append([i[j]-mean_val[j]])
		#print np.dot(np.array(x),np.array(x).T), np.array(x), np.array(x).T
		total+=np.dot(x,np.transpose(x))
		#print total
	return total



def fld_(data, d):
	Points=[]
	label=[]
	cluster=[]
	#seperate Points to label and cluster
	cluster_num = max(data.var[d])
	
	for i in range(int(cluster_num)):
		cluster.append([])

	for i in range(len(data.var[0])):
		coords=[]
		for j in range(d):
			coords.append(data.var[j][i])
		Points.append(coords)
		label.append(int(data.var[d][i]))
		cluster[int(data.var[d][i])-1].append(coords)
	
	mean_val=[]
	for i in cluster:
		mean_vector=[]
		for k in range(d):
			mean_vector.append(0)
		for j in range(len(i)):
			for k in range(d):
				mean_vector[k]+=i[j][k]/len(i)

		#mean_vector = mean_vector/len(i)
		#print mean_vector
		mean_val.append(mean_vector)
	
	#print mean_val
	
	#make W, B
	W=np.zeros((d,d))
	for j in range(len(cluster)):
		W+=sum_W(cluster[j], mean_val[j],d)/float(len(cluster[j]))
		#print W
	
	#print W
	#mean_val
	total_mean=np.zeros((d))

	for i in Points:
		for j in range(d):
			total_mean[j]+=i[j]/float(len(Points))
	#print total_mean
	
	B=np.zeros((d,d))
	for i in range(len(mean_val)):
		x=[]
		for j in range(d):
			x.append([mean_val[i][j]-total_mean[j]])
		B+=len(cluster[i])*np.dot(x,np.transpose(x))

	#print W, B

	T=np.dot(np.linalg.inv(W),B)
	eigenvaluse, eigenvectors = np.linalg.eig(T)
	print eigenvectors
	return eigenvectors
