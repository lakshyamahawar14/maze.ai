import numpy as np
from functions.generators import Generators

class Game:
	mazeSize = (0, 0)
	rowSize = 0
	colSize = 0
	levelMatrix = []
	levelNumber = 0
	difficultyLevel = 0
	numberOfOnes = 0
	visited = []
	isGameOver = True
	isGameFinish = True

	def resetGame(self, screenObj, playerObj, guiObj):
		playerObj.resetPlayer(self.mazeSize, screenObj, guiObj)
		self.visited = [[0 for i in range(self.colSize)] for j in range(self.rowSize)]
		self.visited[0][0] = 1
		self.isGameOver = False
		self.isGameFinish = False

	def loadGame(self, screenObj):
		screenObj.resetScreen()

	def startNewGame(self, screenObj, playerObj, guiObj, inputObj, modelsObj, size=(0, 0)):
		if(size == (0, 0)):
			__random_level = np.random.randint(9,26)
			size = (__random_level, __random_level)
		playerObj.resetPlayer(size, screenObj, guiObj)
		inputObj.rowInput = size[0]
		inputObj.colInput = size[1]
		inputObj.difficultyInput = 1
		return Game(size, modelsObj)
	
	def setLevel(self, levelNumber):
		self.levelNumber = levelNumber

	def updateVisited(self, position, value):
		(i, j) = position
		self.visited[i][j] = value
		
	def __init__(self, mazeSize, modelsObj):
		self.mazeSize = mazeSize
		self.rowSize = self.mazeSize[0]
		self.colSize = self.mazeSize[1]
		generatorObj = Generators()
		(self.levelMatrix, self.numberOfOnes) = generatorObj.generateLevel(self.mazeSize)
		modelInput = [self.rowSize,self.numberOfOnes]
		self.levelNumber= modelsObj.predictDifficulty(modelInput)[0]
		self.visited = [[0 for i in range(self.colSize)] for j in range(self.rowSize)]
		self.visited[0][0] = 1
		self.isGameOver = False
		self.isGameFinish = False