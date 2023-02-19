import numpy as np
from functions.generators import Generators

class Game:
	mazeSize = (0, 0)
	rowSize = 0
	colSize = 0
	levelMatrix = []
	levelNumber= 0
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

	def startNewGame(self, screenObj, playerObj, guiObj, size=(0, 0)):
		if(size == (0, 0)):
			size = (np.random.randint(3, 9), np.random.randint(3, 15))
		playerObj.resetPlayer(size, screenObj, guiObj)
		return Game(size)

	def updateVisited(self, position, value):
		(i, j) = position
		self.visited[i][j] = value
		
	def __init__(self, mazeSize):
		self.mazeSize = mazeSize
		self.rowSize = self.mazeSize[0]
		self.colSize = self.mazeSize[1]
		generatorObj = Generators()
		self.levelMatrix = generatorObj.generateLevel(self.mazeSize)
		self.levelNumber= min(self.rowSize, self.colSize)
		self.visited = [[0 for i in range(self.colSize)] for j in range(self.rowSize)]
		self.visited[0][0] = 1
		self.isGameOver = False
		self.isGameFinish = False