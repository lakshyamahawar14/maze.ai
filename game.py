import pygame
import numpy as np

pygame.init()

screenInfo = pygame.display.Info()
(WIDTH, HEIGHT) = (screenInfo.current_w, screenInfo.current_h)
(X, Y) = (WIDTH, HEIGHT)

RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (75, 0, 255)
GREEN = (0, 255, 75)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)


screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption('MAZE.AI')
screen.fill(BLACK)
logoIcon = pygame.image.load('assets/icons/logo.png')
pygame.display.set_icon(logoIcon)

def initializeScreen():
	global screen
	screen = pygame.display.set_mode((X, Y))
	
def generateRandom(size):
	tempLevelData = []
	row = 2*size[0]+1
	col = size[1]+1
	for i in range(0, row):
		current = []
		isHorizontal = False
		if(i%2 == 0):
			isHorizontal = True
		for j in range(0, col):
			if(isHorizontal == True):
				current.append(2)
				isHorizontal = False
			else:
				if((i == 0 or j == 0) or (i == 2*size[0] or (j == size[1] and i%2 == 1))):
					current.append(1)
					continue
				current.append(np.random.choice(np.arange(0, 2), p=[0.8, 0.2]))
		tempLevelData.append(current)
	return tempLevelData

def generateSemiRandom(size):
	levels = []
	generateSemiRandomHelper(0, size, [], levels)
	randomLevel = levels[np.random.randint(0, len(levels))]
	np.random.shuffle(randomLevel)
	tempLevelData = []
	row = 2*size[0]+1
	col = size[1]+1
	idx = 0
	for i in range(0, row):
		current = []
		isHorizontal = False
		if(i%2 == 0):
			isHorizontal = True
		for j in range(0, col):
			if(isHorizontal == True):
				current.append(2)
				isHorizontal = False
			else:
				if((i == 0 or j == 0) or (i == 2*size[0] or (j == size[1] and i%2 == 1))):
					current.append(1)
					continue
				current.append(randomLevel[idx])
			idx += 1
		tempLevelData.append(current)
	return tempLevelData

def generateSemiRandomHelper(sum, size, levelData, levels):
		density = max(size[0], size[1])
		if(size[0] >= 3 and size[0] < 6):
			density = size[0]*size[0]//2+size[1]
		elif(size[0] >= 6):
			density = size[0]*size[1]
		
		if(sum == density or len(levelData) == (2*size[0]+1)*(size[1]+1)):
			if(len(levelData) == (2*size[0]+1)*(size[1]+1)):
				levels.append(levelData)
			return
		if(np.random.randint(0, 2) == 1):
			levelData.append(1)
			generateSemiRandomHelper(sum+1, size, levelData, levels)
			levelData.pop()
			levelData.append(0)
			generateSemiRandomHelper(sum, size, levelData, levels)
		else:
			levelData.append(0)
			generateSemiRandomHelper(sum, size, levelData, levels)
			levelData.pop()
			levelData.append(1)
			generateSemiRandomHelper(sum+1, size, levelData, levels)
		return

def isMovePossible(i, j, di, dj, size, levelData):
	x_pos = X//2-size[1]*game.lineLength//2+game.lineLength//2+game.lineLength*j
	y_pos = Y//2-game.lineLength//2+game.lineLength*i
	u = levelData[2*i][j+1]
	d = levelData[2*i+2][j+1]
	l = levelData[2*i+1][j]
	r = levelData[2*i+1][j+1]
	if(di == 1):
		if(y_pos+game.lineLength > Y//2-(3*game.lineLength)//2+game.lineLength*size[0] or d == 1):
			return False
	elif(di == -1):
		if(y_pos-game.lineLength < Y//2-game.lineLength//2 or u == 1):
			return False
	elif(dj == 1):
		if(x_pos+game.lineLength > X//2-game.lineLength//2+game.lineLength//2*size[1] or r == 1):
			return False
	elif(dj == -1):
		if(x_pos-game.lineLength < X//2+game.lineLength//2-game.lineLength//2*size[1] or l == 1):
			return False
	return True

def isStructured(size, levelData):
    return True

def generateLevel(size):
	data = []
	while True:
		# data = generateRandom(size)
		data = generateSemiRandom(size)
		if(isStructured(size, data) == True):
			break
	return data

class Game:
	levelData = []
	mazeSize = (0, 0)
	level = 0
	x_player = 0
	y_player = 0
	visited = []
	isGameOver = True
	isGameFinish = True
	fontSize = 0
	lineLength = 0
	lineWidth = 0

	def __init__(self, _mazeSize):
		self.fontSize = 32
		self.lineLength = 50
		self.lineWidth = 5
		self.mazeSize = _mazeSize
		self.levelData = generateLevel(self.mazeSize)
		self.level = min(self.mazeSize[0], self.mazeSize[1])
		self.x_player = X//2-self.mazeSize[1]*self.lineLength//2+self.lineLength//2
		self.y_player = Y//2-self.lineLength//2
		self.visited = [[0 for i in range(self.mazeSize[1])] for j in range(self.mazeSize[0])]
		self.visited[0][0] = 1
		self.isGameOver = False
		self.isGameFinish = False

	def reset(self):
		self.x_player = X//2-self.mazeSize[1]*self.lineLength//2+self.lineLength//2
		self.y_player = Y//2-self.lineLength//2
		self.visited = [[0 for i in range(self.mazeSize[1])] for j in range(self.mazeSize[0])]
		self.visited[0][0] = 1
		self.isGameOver = False
		self.isGameFinish = False

	def updatePlayer(self, x, y):
		self.x_player = x
		self.y_player = y

	def updateVisited(self, i, j, val):
		self.visited[i][j] = val

game = Game((np.random.randint(3, 9), np.random.randint(3, 15)))

def drawHeadText():
	font = pygame.font.Font(None, game.fontSize+12)
	headText = font.render('MAZE.AI', True, GREEN, BLACK)
	headRect = headText.get_rect()
	headRect.center = (X//2, 50)
	screen.blit(headText, headRect)

def drawLevelText():
	font = pygame.font.Font(None, game.fontSize)
	levelText = font.render(f'LEVEL: {game.level}', True, GREEN, BLACK)
	levelRect = levelText.get_rect()
	levelRect.center = (X//2, 150)
	screen.blit(levelText, levelRect)

def drawPlayer():
	pygame.draw.line(screen, RED, (game.x_player-game.lineWidth, game.y_player), (game.x_player+game.lineWidth, game.y_player), game.lineWidth)

def isValid(u, d, l, r, key):
	if(key == 119):
		if(game.y_player-game.lineLength < Y//2-game.lineLength//2 or u == 1):
			return False
		return True
	elif(key == 115):
		if(game.y_player+game.lineLength > Y//2-(3*game.lineLength)//2+game.lineLength*game.mazeSize[0] or d == 1):
			return False
		return True
	elif(key == 97):
		if(game.x_player-game.lineLength < X//2+game.lineLength//2-game.lineLength//2*game.mazeSize[1] or l == 1):
			return False
		return True
	elif(key == 100):
		if(game.x_player+game.lineLength > X//2-game.lineLength//2+game.lineLength//2*game.mazeSize[1] or r == 1):
			return False
		return True
	return False

def movePlayer(key):
	j = (game.x_player-(X//2-game.mazeSize[1]*game.lineLength//2+game.lineLength//2))//game.lineLength
	i = (game.y_player-(Y//2-game.lineLength//2))//game.lineLength
	u = game.levelData[2*i][j+1]
	d = game.levelData[2*i+2][j+1]
	l = game.levelData[2*i+1][j]
	r = game.levelData[2*i+1][j+1]
	if(isValid(u, d, l, r, key) == False):
		return
	game.updateVisited(i, j, 1)
	if(key == 119):
		i -= 1
		game.updatePlayer(game.x_player, game.y_player-game.lineLength)
	elif(key == 115):
		i += 1
		game.updatePlayer(game.x_player, game.y_player+game.lineLength)
	elif(key == 97):
		j -= 1
		game.updatePlayer(game.x_player-game.lineLength, game.y_player)
	elif(key == 100):
		j += 1
		game.updatePlayer(game.x_player+game.lineLength, game.y_player)

	if(i == game.mazeSize[0]-1 and j == game.mazeSize[1]-1):
		game.isGameFinish = True
	if(game.visited[i][j] == 1):
		game.isGameOver = True

def drawVisited():
	row = game.mazeSize[0]
	col = game.mazeSize[1]
	for i in range(row):
		for j in range(col):
			if(game.visited[i][j] == 1):
				x_visited = X//2-game.mazeSize[1]*game.lineLength//2+game.lineLength//2+game.lineLength*j
				y_visited = Y//2-game.lineLength//2+game.lineLength*i
				pygame.draw.line(screen, YELLOW, (x_visited-2, y_visited), (x_visited+2, y_visited), game.lineWidth)

def drawVertical(value, x, y, offset=game.lineLength):
	if(value == 0):
		return
	pygame.draw.line(screen, GREEN, (x, y), (x, y+offset), game.lineWidth)

def drawHorizontal(value, x, y, offset=game.lineLength):
	if(value == 0):
		return
	pygame.draw.line(screen, GREEN, (x, y), (x+offset, y), game.lineWidth)

def drawLine(type, value, x, y):
	if(type != 2):
		drawVertical(value, x, y)
	else:
		drawHorizontal(value, x, y)

def drawMaze():
	(x, y) = (X//2-game.lineLength//2*game.mazeSize[1], Y//2-game.lineLength)
	for i in range(0, len(game.levelData)):
		isHorizontal = False
		isVertical = False
		for j in range(0, len(game.levelData[0])):
			if(isHorizontal == True):
				drawLine(2, game.levelData[i][j], x, y)
				x += game.lineLength

			if(game.levelData[i][j] == 2 and isHorizontal == False):
				isHorizontal = True
			elif(isHorizontal == False and isVertical == False):
				isVertical = True

			if(isVertical == True):
				drawLine(1, game.levelData[i][j], x, y)
				x += game.lineLength

		if(isVertical == True):
			y += game.lineLength
			x -= game.lineLength*(game.mazeSize[1]+1)
		else:
			x -= game.lineLength*game.mazeSize[1]

def createTextBox(font, text, textColor, boxColor, margin_x, margin_y):
    textSurf = font.render(text, True, textColor, boxColor)
    boxSurf = pygame.Surface(textSurf.get_rect().inflate(margin_x, margin_y).size)
    boxSurf.fill(boxColor)
    boxSurf.blit(textSurf, textSurf.get_rect(center = boxSurf.get_rect().center))
    return boxSurf

def drawReset():
	font = pygame.font.Font(None, game.fontSize)
	text_surf = createTextBox(font, "RESET", BLACK, YELLOW, 10, 10)
	screen.blit(text_surf, text_surf.get_rect(center = (100, 50)))

def drawRegenerate():
	font = pygame.font.Font(None, game.fontSize)
	text_surf = createTextBox(font, "REGENERATE", WHITE, BLUE, 10, 10)
	screen.blit(text_surf, text_surf.get_rect(center = (300, 50)))

def drawPlayAgain():
	font = pygame.font.Font(None, game.fontSize)
	textSurf = createTextBox(font, "PLAY AGAIN", BLACK, GREEN, 10, 10)
	screen.blit(textSurf, textSurf.get_rect(center = (X//2, Y//2-100)))

def drawQuit():
	font = pygame.font.Font(None, game.fontSize)
	text_surf = createTextBox(font, "QUIT", WHITE, RED, 10, 10)
	screen.blit(text_surf, text_surf.get_rect(center = (X-100, 50)))

def isResetClicked(pos):
	if(pos[0] > 100-45 and pos[0] < 100+40 and pos[1] > 50-20 and pos[1] < 50+15):
		return True
	return False

def isRegenerateClicked(pos):
	if(pos[0] > 300-83 and pos[0] < 300+83 and pos[1] > 50-20 and pos[1] < 50+20):
		return True
	return False

def isPlayAgainClicked(isGameOver, pos):
	if(isGameOver == True and pos[0] > X//2-50-25 and pos[0] < X//2+50+25 and pos[1] > Y//2-100-15 and pos[1] < Y//2-100+15):
		return True
	return False

def isQuitClicked(pos):
	if(pos[0] > X-100-35 and pos[0] < X-100+30 and pos[1] > 50-20 and pos[1] < 50+15):
		return True
	return False

def drawGameOver():
	font = pygame.font.Font(None, game.fontSize)
	gameOverText = font.render('Game Over!', True, RED, BLACK)
	gameOverRect = gameOverText.get_rect()
	gameOverRect.center = (X//2, Y//2-150)
	screen.blit(gameOverText, gameOverRect)

def resetMaze():
	game.reset()

def startNewGame():
	global game
	randomLevel = (np.random.randint(3, 9), np.random.randint(3, 15))
	game = Game(randomLevel)

def drawFinish():
	font = pygame.font.Font(None, game.fontSize)
	finishText = font.render('Victory!', True, GREEN, BLACK)
	finishRect = finishText.get_rect()
	finishRect.center = (X//2, Y//2-150)
	screen.blit(finishText, finishRect)

def loadLevel():
	initializeScreen()
	drawMaze()

while True:
	loadLevel()
	drawReset()
	drawRegenerate()
	drawQuit()
	drawVisited()
	drawPlayer()
	if game.isGameOver == True:
		drawGameOver()
		drawPlayAgain()
	elif game.isGameFinish == True:
		drawFinish()
		drawPlayAgain()
	else:
		drawHeadText()
		drawLevelText()
		drawMaze()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		if event.type == pygame.KEYDOWN and game.isGameOver == False and game.isGameFinish == False:
			movePlayer(event.key)
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			if(isResetClicked(pos) == True):
				resetMaze()
			if(isPlayAgainClicked(game.isGameOver or game.isGameFinish, pos) == True or isRegenerateClicked(pos) == True):
				startNewGame()	
			if(isQuitClicked(pos) == True):
				pygame.quit()
				quit()
			

	pygame.display.update()
