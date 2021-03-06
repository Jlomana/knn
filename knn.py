# Example of kNN implemented from Scratch in Python2x
 
import csv
import random
import math
import operator
 
def loadDataset(filename, split, trainingSet=[] , testSet=[]):
	with open(filename, 'rb') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(len(dataset)-1):
	        for y in range(4):
	            dataset[x][y] = float(dataset[x][y])
	        trainingSet.append(dataset[x])
 
def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((float(instance1[x]) - float(instance2[x])), 2)
	return math.sqrt(distance)
 
def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	"""setosa=0
	versicolor=0
	virginica=0
	for x in range(len(neighbors)):
		if neighbors[x][4]=="Iris-setosa":
			setosa+=1
		elif neighbors[x][4]=="Iris-versicolor":
			versicolor+=1
		elif neighbors[x][4]=="Iris-virginica":
			virginica+=1
	print("Iris-setosa is ")
	print(setosa)
	print("Iris-versicolor is ")
	print(versicolor)
	print("Iris-virginica is ")
	print(virginica)"""
	return neighbors
 
def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]
 
"""def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0"""
	
def main():
	trainingSet=[]
	line = raw_input()
	line = line.split(",")
	lines = [line]
	testSet=[]
	dataset = lines
	testSet = dataset
	split=0.67
	loadDataset('iris.txt', split, trainingSet, testSet)
	predictions=[]
	k = 20
	for x in range(len(testSet)):
		neighbors = getNeighbors(trainingSet, testSet[x], k)
		result = getResponse(neighbors)
		predictions.append(result)
		print("The flower is ")
		print(repr(result))
	#accuracy = getAccuracy(testSet, predictions)
	#print('Accuracy: ' + repr(accuracy) + '%')
	
main()