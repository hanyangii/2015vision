import numpy as np
from matplotlib import pyplot as plt
from kmeans import *
from pca import *
from spectral import *
from fld import *

class datas:
	def __init__(self,d):
		self.var=[[] for x in range(d+1)]

	def append_var(self, i, val):
		self.var[i].append(val)

openfile = open("spiral.txt","r")
d=2
k=3
#data=data(2)
i=0

data=[]
label=[]
while True:
	line = openfile.readline()
	if not line: break
	line=line.split('	')
	#print line
	x=[]
	for i in range(d):
		#print i, line[i]
		x.append(float(line[i]))
		#data.append_var(i,float(line[i]))
	data.append(x)
	label.append(line[d])
	#data.append([float(line[0]),float(line[1]),float(line[2])])
affinity_matrix =affinity(data,k,d)

def nolabel(data,d):
	datas_=datas(d)
	for i in data:
		for j in range(d):
			datas_.append_var(j, float(i[j]))
	return datas_

def labelling(data,label,d):
	datas_=datas(d)
	for i in data:
		for j in range(d):
			datas_.append_var(j, float(i[j]))
	
	for i in label:
		datas_.append_var(d,float(i))
	return datas_
			
def pca(data,d):
	data_ = nolabel(data, d)
	pca_(data_, d)

def fld(data,label,d):
	data_ = labelling(data,label,d)
	fld_(data_, d)

def k_means_clustering(data,k):
	d=len(data[0])
	data_=nolabel(data,d)
	k_means_clustering_(data_,k,d)

def spectral_clustering(affinity_matrix,k):
	spectral_clustering_(affinity_matrix, k)


y=pca(data,d)
y=fld(data,label,d)
labels=k_means_clustering(data,k)
labels=spectral_clustering(affinity_matrix, k)
