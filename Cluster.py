import fasttext
import fasttext.util
from MyText import Text
from MyText import *
import numpy as np
from math import sqrt

class Cluster:

	def __init__(self,model,textinstance):
		self.model = model
		self.textlist = list()
		self.textlist.append(textinstance)
		self.averagevector = textinstance.GetVector()

	def avg(self):
		s = sum(map(lambda x: x.GetVector(), textlist))
		a = s / len(textlist)
		return a
	#def CountAverageVector(self):     #recalculation of average vector
	#	textnums = 0
	#	sumvector = 0
	#	
	#	for text in self.textlist:
	#		sumvector = sumvector + text.GetVector()
	#		textnums = textnums + 1
#
#	#	for i in sumvector:
#	#		i = i/textnums
#
	#	self.averagevector = sumvector
	
	def CountAverageVector(self):
		return self.averagevector
	
	def GetSize(self):
		return len(self.textlist)


	def AppendText(self,textinstance):
		self.textlist.append(textinstance)
		self.CountAverageVector()



class Characteristics:
	def __init__(self):
		self.distance = 0
		self.clustername = ""
		

class ClusterDispatcher:
	def __init__(self):
		self.clusters = dict()#dictionary for clusters
	
	def GetClustersnum(self):
		return len(self.clusters)
		
	def AppendCluster(self,clustername,cluster:Cluster):
		self.clusters[clustername] = cluster 

	def CountDistance(self,vector1,vector2):
		square = np.square(vector1 - vector2)
		sum_square = np.sum(square)
		
		distance = sqrt(sum_square)
		return distance

	def FindMin(self,textinstance:Text):
		characteristics = Characteristics()
		characteristics.clustername = list(self.clusters.keys())[0]
		characteristics.distance = self.CountDistance(self.clusters[characteristics.clustername].averagevector,textinstance.GetVector())

		for i in self.clusters.keys():
			if (characteristics.distance < self.CountDistance(self.clusters[i].averagevector,textinstance.GetVector())):
				characteristics.clustername = i
				characteristics.distance = self.CountDistance(self.clusters[i].averagevector,textinstance.GetVector())
		
		return characteristics 

	def Distribute(self,textinstance:Text):
		characteristics = self.FindMin(textinstance)
		self.clusters[characteristics.clustername].AppendText(textinstance)
			
		
		


	
		