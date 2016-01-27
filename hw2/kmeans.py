import numpy as np
import matplotlib.pyplot as plt
import math
import random

class Point:
	def __init__(self, coords, label):
		self.coords=coords
		self.label=label
	
	def __repr__(self):
		return str(self.coords)+' '+str(self.label)

def getKey(item):
	return item[2]

def getDistance(a,b, d):
	sum_val = 0
	for i in range(d):
		sum_val += pow((a.coords[i]-b.coords[i]),2)
	return math.sqrt(sum_val)

def kmeans(Points, k_,d):
	initial = random.sample(Points, k_)
	#print initial
	clusters = initial

	while True:
		oldclusters = clusters
		lists=[]
		for t in range(k_):
			lists.append([])
		for p in Points:
			min_distance = getDistance(p, clusters[0], d)
			
			index=0
			for j in range(len(clusters[1:])):
				distance = getDistance(p, clusters[j+1],d)
				if distance<min_distance:
					min_distance=distance
					index = j+1
			
			#print index, len(lists)
			#print lists
			lists[index].append(p)
			p.label=index
		
		#find new means
		cluster_list=[]
		for l in lists:
			coords=[]
			for i in range(d):
				#print l
				tmp=[]
				for t in l:
					tmp.append(t.coords[i])
				#print tmp
				coords.append(np.mean(tmp))
			cluster_point = Point(coords, lists.index(l))
			cluster_list.append(cluster_point)
		clusters=cluster_list
		isend=0
		for k in range(len(cluster_list)):
			if cmp(oldclusters[k].coords, cluster_list[k].coords)==0:
				isend+=1
		if isend==k_:
			break
	return lists, Points



def k_means_clustering_(data_,k,d):
	Points_num=0
	Points=[]
	for i in range(len(data_.var[0])):
		Points_num+=1
		coords=[]
		for j in range(d):
			coords.append(data_.var[j][i])
		point=Point(coords,None)
		Points.append(point)
	
	#print Points[0]
	
	afterPoints, result=kmeans(Points, k, d)
	#print afterPoints
	
	label=[]
	for i in result:
		label.append(i.label)
	
	if not d==2: return label

	colors = ["orange","violet","brown","skyblue","yellowgreen","gray","ivory","navy","red","blue","green","yellow","black","purple","pink"]

	for t in afterPoints:
		di=[]
		for i in range(d):
			di.append([])

		for tt in t:
			for i in range(d):
				#print tt
				di[i].append(tt.coords[i])

		plt.plot(di[0], di[1],'o', markersize=5, color=colors[afterPoints.index(t)],alpha=1)
	
	plt.legend()
	plt.show()
	
	print label
	return label
