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

	def generateManual(self, gameObj):
		rowSize = gameObj.rowSize
		colSize = gameObj.colSize
		size = (rowSize, colSize)
		gameObj.startNewGame(size)

	def generateLevel(self, size):
		return self.generateRandom(size)
	
	def __init__(self):
		pass