#Python3x
import csv
import math
import operator

def loadDataset(filename, trainingSet=[], testSet=[]):
	with open(filename, 'r') as csvfile:
		lines=csv.reader(csvfile)
		dataset=list(lines)
		for x in range(len(dataset)):
				for y in range(4):
					dataset[x][y]=float(dataset[x][y])
				trainingSet.append(dataset[x])

def euclideanDistance(instance1, instance2, length):
	distance=0
	for x in range(length):
		distance += math.pow(float(instance1[x]) - float(instance2[x]), 2)
	return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
	distances=[]
	length=len(testInstance)
	for x in range(len(trainingSet)):
		dist=euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors=[]
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

def getResponse(neighbors):
	classVotes={}
	for x in range(len(neighbors)):
		response=neighbors[x][-1]
		if response in classVotes:
			classVotes[response]+=1
		else:
			classVotes[response]=1
	sortedVotes=sorted(classVotes, key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0]

def main():
	trainingSet=[]
	print("Enter data: ")
	line=input().split(",")
	print("Enter k: ")
	k=int(input())
	testSet=[]
	testSet=[line]
	loadDataset('iris.txt', trainingSet, testSet)
	for x in range(len(testSet)):
		neighbors=getNeighbors(trainingSet, testSet[x], k)
		result=getResponse(neighbors)
		print(repr(result))

main()