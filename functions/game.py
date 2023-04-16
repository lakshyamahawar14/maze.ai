import numpy as np

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

	def startNewGame(self, screenObj, playerObj, guiObj, inputObj, modelsObj, generatorsObj, solversObj, paramsObj, size=(0, 0)):
		if(size == (0, 0)):
			__random_level = np.random.randint(9,26)
			size = (__random_level, __random_level)
		playerObj.resetPlayer(size, screenObj, guiObj)
		inputObj.rowInput = size[0]
		inputObj.rowInput = size[1]
		inputObj.difficultyInput = 1
		solversObj.solutionPath = []
		return Game(size, modelsObj, generatorsObj, solversObj, paramsObj)
	
	def setLevel(self, levelNumber):
		self.levelNumber = levelNumber

	def updateVisited(self, position, value):
		(i, j) = position
		self.visited[i][j] = value
		
	def __init__(self, mazeSize, modelsObj, generatorsObj, solversObj, paramsObj):
		self.mazeSize = mazeSize
		self.rowSize = self.mazeSize[0]
		self.colSize = self.mazeSize[1]
		(self.levelMatrix, self.numberOfOnes) = generatorsObj.generateLevel(self.mazeSize)
		solversObj.solutionPath = solversObj.backtrackingSolver(generatorsObj.generatorObj)
		wallDensity = paramsObj.getWallDensity(self)
		branchingFactor = paramsObj.getBranchingFactor(self)
		solutionDistortions = paramsObj.getSolutionDistortions(solversObj)
		MSTCost = paramsObj.getMSTCost(generatorsObj.generatorObj)
		modelInput = [mazeSize[0], wallDensity, branchingFactor, solutionDistortions, MSTCost]
		self.levelNumber= modelsObj.predictDifficulty(modelInput)[0]
		self.visited = [[0 for i in range(self.colSize)] for j in range(self.rowSize)]
		self.visited[0][0] = 1
		self.isGameOver = False
		self.isGameFinish = False