import pygame
import numpy as np

pygame.init()

screenInfo = pygame.display.Info()
(WIDTH, HEIGHT) = (screenInfo.current_w, screenInfo.current_h)

RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 100)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
(X, Y) = (WIDTH, HEIGHT)

def initializeScreen():
	screen = pygame.display.set_mode((X, Y))
	pygame.display.set_caption('MAZE.AI')
	screen.fill(BLACK)
	logoIcon = pygame.image.load('assets/icons/logo.png')
	pygame.display.set_icon(logoIcon)

screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption('MAZE.AI')
screen.fill(BLACK)
logoIcon = pygame.image.load('assets/icons/logo.png')
pygame.display.set_icon(logoIcon)
	
def generateRandom(size):
	tempLevelData = []
	row = 2*size+1
	col = size+1
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
				if((i == 0 or j == 0) or (i == 2*size or (j == size and i%2 == 1))):
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
	row = 2*size+1
	col = size+1
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
				if((i == 0 or j == 0) or (i == 2*size or (j == size and i%2 == 1))):
					current.append(1)
					continue
				current.append(randomLevel[idx])
			idx += 1
		tempLevelData.append(current)
	return tempLevelData

def generateSemiRandomHelper(sum, size, levelData, levels):
		density = size
		if(size >= 3 and size < 6):
			density = size*size//2+size
		elif(size >= 6):
			density = size*size
		
		if(sum == density or len(levelData) == (2*size+1)*(size+1)):
			if(len(levelData) == (2*size+1)*(size+1)):
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
	x_pos = X//2-size*25+25+50*j
	y_pos = Y//2-25+50*i
	u = levelData[2*i][j+1]
	d = levelData[2*i+2][j+1]
	l = levelData[2*i+1][j]
	r = levelData[2*i+1][j+1]
	if(di == 1):
		if(y_pos+50 > Y//2-75+50*size or d == 1):
			return False
	elif(di == -1):
		if(y_pos-50 < Y//2-25 or u == 1):
			return False
	elif(dj == 1):
		if(x_pos+50 > X//2-25+25*size or r == 1):
			return False
	elif(dj == -1):
		if(x_pos-50 < X//2+25-25*size or l == 1):
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
	mazeSize = 0
	level = mazeSize
	x_player = 0
	y_player = 0
	visited = []
	isGameOver = True
	isGameFinish = True

	def __init__(self, _mazeSize):
		self.mazeSize = _mazeSize
		self.levelData = generateLevel(self.mazeSize)
		self.level = self.mazeSize
		self.x_player = X//2-self.mazeSize*25+25
		self.y_player = Y//2-25
		self.visited = [[0 for i in range(self.mazeSize)] for j in range(self.mazeSize)]
		self.visited[0][0] = 1
		self.isGameOver = False
		self.isGameFinish = False

	def updatePlayer(self, x, y):
		self.x_player = x
		self.y_player = y

	def updateVisited(self, i, j, val):
		self.visited[i][j] = val

game = Game(np.random.randint(3, 8))

def drawHeadText():
	font = pygame.font.Font(None, 32)
	headText = font.render('MAZE.AI', True, GREEN, BLACK)
	headRect = headText.get_rect()
	headRect.center = (X//2, 50)
	screen.blit(headText, headRect)

def drawLevelText(level):
	font = pygame.font.Font(None, 24)
	levelText = font.render(f'Level: {level}', True, GREEN, BLACK)
	levelRect = levelText.get_rect()
	levelRect.center = (X//2, 150)
	screen.blit(levelText, levelRect)

def drawPlayer():
	pygame.draw.line(screen, RED, (game.x_player-5, game.y_player), (game.x_player+5, game.y_player), 5)

def isValid(u, d, l, r, key):
	if(key == 119):
		if(game.y_player-50 < Y//2-25 or u == 1):
			return False
		return True
	elif(key == 115):
		if(game.y_player+50 > Y//2-75+50*game.mazeSize or d == 1):
			return False
		return True
	elif(key == 97):
		if(game.x_player-50 < X//2+25-25*game.mazeSize or l == 1):
			return False
		return True
	elif(key == 100):
		if(game.x_player+50 > X//2-25+25*game.mazeSize or r == 1):
			return False
		return True
	return False

def movePlayer(key):
	j = (game.x_player-(X//2-game.mazeSize*25+25))//50
	i = (game.y_player-(Y//2-25))//50
	u = game.levelData[2*i][j+1]
	d = game.levelData[2*i+2][j+1]
	l = game.levelData[2*i+1][j]
	r = game.levelData[2*i+1][j+1]
	if(isValid(u, d, l, r, key) == False):
		return
	game.updateVisited(i, j, 1)
	if(key == 119):
		i -= 1
		game.updatePlayer(game.x_player, game.y_player-50)
	elif(key == 115):
		i += 1
		game.updatePlayer(game.x_player, game.y_player+50)
	elif(key == 97):
		j -= 1
		game.updatePlayer(game.x_player-50, game.y_player)
	elif(key == 100):
		j += 1
		game.updatePlayer(game.x_player+50, game.y_player)

	if(i == game.mazeSize-1 and j == game.mazeSize-1):
		game.isGameFinish = True

	if(game.visited[i][j] == 1):
		game.isGameOver = True

def drawVisited():
	for i in range(game.mazeSize):
		for j in range(game.mazeSize):
			if(game.visited[i][j] == 1):
				x_visited = X//2-game.mazeSize*25+25+50*j
				y_visited = Y//2-25+50*i
				pygame.draw.line(screen, YELLOW, (x_visited-2, y_visited), (x_visited+2, y_visited), 5)

def drawVertical(value, x, y, offset=50):
	if(value == 0):
		return
	pygame.draw.line(screen, GREEN, (x, y), (x, y+offset), 5)

def drawHorizontal(value, x, y, offset=50):
	if(value == 0):
		return
	pygame.draw.line(screen, GREEN, (x, y), (x+offset, y), 5)

def drawLine(type, value, x, y):
	if(type != 2):
		drawVertical(value, x, y)
	else:
		drawHorizontal(value, x, y)

def drawMaze(mazeSize, levelData):
	(x, y) = (X//2-25*mazeSize, Y//2-50)
	for i in range(0, len(levelData)):
		isHorizontal = False
		isVertical = False
		for j in range(0, len(levelData[0])):
			if(isHorizontal == True):
				drawLine(2, levelData[i][j], x, y)
				x += 50

			if(levelData[i][j] == 2 and isHorizontal == False):
				isHorizontal = True
			elif(isHorizontal == False and isVertical == False):
				isVertical = True

			if(isVertical == True):
				drawLine(1, levelData[i][j], x, y)
				x += 50

		if(isVertical == True):
			y += 50
			x -= 50*(mazeSize+1)
		else:
			x -= 50*mazeSize

def createTextBox(font, text, text_color, box_color, margin_x, margin_y):
    text_surf = font.render(text, True, text_color, box_color)
    box_surf = pygame.Surface(text_surf.get_rect().inflate(margin_x, margin_y).size)
    box_surf.fill(box_color)
    box_surf.blit(text_surf, text_surf.get_rect(center = box_surf.get_rect().center))
    return box_surf

def drawPlayAgain():
	font = pygame.font.Font(None, 24)
	text_surf = createTextBox(font, "PLAY AGAIN", BLACK, GREEN, 10, 10)
	screen.blit(text_surf, text_surf.get_rect(center = (X//2, Y//2-100)))

def drawQuit():
	font = pygame.font.Font(None, 24)
	text_surf = createTextBox(font, "QUIT", WHITE, RED, 10, 10)
	screen.blit(text_surf, text_surf.get_rect(center = (X-100, 50)))

def isPlayAgainClicked(isGameOver, pos):
	if(isGameOver == True and pos[0] > X//2-50-10 and pos[0] < X//2+50+10 and pos[1] > Y//2-100-12 and pos[1] < Y//2-100+12):
		return True
	return False

def isQuitClicked(pos):
	if(pos[0] > X-100-25 and pos[0] < X-100+25 and pos[1] > 50-12 and pos[1] < 50+12):
		return True
	return False

def drawGameOver():
	font = pygame.font.Font(None, 24)
	gameOverText = font.render('Game Over!', True, RED, BLACK)
	gameOverRect = gameOverText.get_rect()
	gameOverRect.center = (X//2, Y//2-150)
	screen.blit(gameOverText, gameOverRect)

def startNewGame():
	global game
	initializeScreen()
	randomLevel = np.random.randint(3, 8)
	game = Game(randomLevel)

def drawFinish():
	font = pygame.font.Font(None, 24)
	finishText = font.render('Victory!', True, GREEN, BLACK)
	finishRect = finishText.get_rect()
	finishRect.center = (X//2, Y//2-150)
	screen.blit(finishText, finishRect)

def loadLevel():
	screen.fill(BLACK)
	drawMaze(game.mazeSize, game.levelData)

while True:
	loadLevel()
	drawVisited()
	drawPlayer()
	drawQuit()
	if game.isGameOver == True:
		drawGameOver()
		drawPlayAgain()
	elif game.isGameFinish == True:
		drawFinish()
		drawPlayAgain()
	else:
		drawHeadText()
		drawLevelText(game.level)
		drawMaze(game.mazeSize, game.levelData)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		if event.type == pygame.KEYDOWN and game.isGameOver == False and game.isGameFinish == False:
			movePlayer(event.key)
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			if(isPlayAgainClicked(game.isGameOver or game.isGameFinish, pos) == True):
				startNewGame()	
			if(isQuitClicked(pos) == True):
				pygame.quit()
				quit()
			

	pygame.display.update()
