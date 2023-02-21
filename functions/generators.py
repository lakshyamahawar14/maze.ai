import numpy as np

class Generators:
	def generateRandom(self, size):
		row = 2*size[0]-1
		col = 2*size[1]-1
		levelMatrix = [[0 for i in range(col)] for j in range(row)]
		
		for i in range(row):
			for j in range(col):
				if i%2 == 0 and j%2 == 0:
					levelMatrix[i][j] = 0
				elif i%2 == 1 and j%2 == 1:
					levelMatrix[i][j] = -1
				else:
					levelMatrix[i][j] = np.random.randint(0, 2)
					
		return levelMatrix

	def findUniquePathsHelper(self, i, j, r, c, levelMatrix):
		if(i == r or j == c):
			return 0
		if(levelMatrix[i][j] != 0):
			return 0
		if(i == r-1 and j == c-1):
			return 1
		return  self.findUniquePathsHelper(i+1, j, r, c, levelMatrix) + self.findUniquePathsHelper(i, j+1, r, c, levelMatrix)

	def findUniquePaths(self, levelMatrix):
		r,c = len(levelMatrix),len(levelMatrix[0])
		return self.findUniquePathsHelper(0, 0, r, c, levelMatrix)

	def generateManual(self, gameObj):
		rowSize = gameObj.rowSize
		colSize = gameObj.colSize
		size = (rowSize, colSize)
		gameObj.startNewGame(size)

	def generateLevel(self, size):
		levelMatrix = []
		countpaths = 0
		while(True):
			levelMatrix = self.generateRandom(size)
			countpaths = self.findUniquePaths(levelMatrix)
			if(countpaths != 0):
				break
		countones = 0
		for i in range(size[0]):
			for j in range(size[1]):
				countones += levelMatrix[i][j]==1
		return (levelMatrix, countpaths, countones)
	
	def __init__(self):
		pass