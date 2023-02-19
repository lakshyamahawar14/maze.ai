import pygame
from functions.colors import RED, BLACK, PURPLE, GREEN, PINK, YELLOW, WHITE

class GUI:
    fontSize = 32
    lineLength = 50
    lineWidth = 5

    def setFontSize(self, fontSize):
        self.fontSize = fontSize

    def setLineLength(self, lineLength):
        self.lineLength = lineLength

    def setLineWidth(self, lineWidth):
        self.lineWidth = lineWidth

    def drawHeadText(self, screenObj):
        (X, Y) = screenObj.getScreenSize()
        screen = screenObj.screen
        font = pygame.font.Font(None, self.fontSize+12)
        headText = font.render('MAZE.AI', True, GREEN, BLACK)
        headRect = headText.get_rect()
        headRect.center = (X//2, 50)
        screen.blit(headText, headRect)

    def drawLevelText(self, screenObj, gameObj):
        (X, Y) = screenObj.getScreenSize()
        screen = screenObj.screen
        font = pygame.font.Font(None, self.fontSize)
        levelText = font.render(f'LEVEL: {gameObj.levelNumber}', True, GREEN, BLACK)
        levelRect = levelText.get_rect()
        levelRect.center = (X//2, 150)
        screen.blit(levelText, levelRect)

    def drawHorizontalLine(self, position, offset, screenObj):
        screen = screenObj.screen
        (x, y) = position
        pygame.draw.line(screen, GREEN, (x, y), (x+offset, y), self.lineWidth)

    def drawVerticalLine(self, position, offset, screenObj):
        screen = screenObj.screen
        (x, y) = position
        pygame.draw.line(screen, GREEN, (x, y), (x, y+offset), self.lineWidth)

    def drawMaze(self, screenObj, gameObj):
        (X, Y) = screenObj.getScreenSize()
        rowSize = gameObj.rowSize
        colSize = gameObj.colSize
        levelMatrix = gameObj.levelMatrix
        (x, y) = (X//2-self.lineLength//2*colSize, Y//2-self.lineLength)

        for i in range(colSize):
            self.drawHorizontalLine((x, y), self.lineLength, screenObj)
            x += self.lineLength
        for i in range(rowSize):
            self.drawVerticalLine((x, y), self.lineLength, screenObj)
            y += self.lineLength
        for i in range(colSize):
            self.drawHorizontalLine((x, y), -self.lineLength, screenObj)
            x -= self.lineLength
        for i in range(rowSize):
            self.drawVerticalLine((x, y), -self.lineLength, screenObj)
            y -= self.lineLength
        
        row = 2*rowSize-1
        col = 2*colSize-1

        for i in range(row):
            if(i%2 == 0):
                x += self.lineLength
            for j in range(col):
                if(i%2 == 0 and j%2 == 0):
                    continue
                if(i%2 == 1 and j%2 == 1):
                    continue
                if i%2 == 0 and j%2 == 1 and levelMatrix[i][j] == 1:
                    self.drawVerticalLine((x, y), self.lineLength, screenObj)
                elif i%2 == 1 and j%2 == 0 and levelMatrix[i][j] == 1:
                    self.drawHorizontalLine((x, y), self.lineLength, screenObj)
                x += self.lineLength
            if(i%2 == 0):
                y += self.lineLength
            x -= colSize*self.lineLength


    def drawPlayer(self, screenObj, playerObj):
        screen = screenObj.screen
        pygame.draw.line(screen, RED, (playerObj.x_player-self.lineWidth, playerObj.y_player), (playerObj.x_player+self.lineWidth, playerObj.y_player), self.lineWidth)

    def drawVisited(self, screenObj, gameObj):
        (X, Y) = screenObj.getScreenSize()
        rowSize = gameObj.rowSize
        colSize = gameObj.colSize
        screen = screenObj.screen

        for i in range(rowSize):
            for j in range(colSize):
                if(gameObj.visited[i][j] == 1):
                    x_visited = X//2-colSize*self.lineLength//2+self.lineLength//2+self.lineLength*j
                    y_visited = Y//2-self.lineLength//2+self.lineLength*i
                    pygame.draw.line(screen, YELLOW, (x_visited-self.lineWidth//2, y_visited), (x_visited+self.lineWidth//2, y_visited), self.lineWidth)

    def createTextBox(self, text, textColor, boxColor, margin_x, margin_y):
        font = pygame.font.Font(None, self.fontSize)
        textSurf = font.render(text, True, textColor, boxColor)
        boxSurf = pygame.Surface(textSurf.get_rect().inflate(margin_x, margin_y).size)
        boxSurf.fill(boxColor)
        boxSurf.blit(textSurf, textSurf.get_rect(center = boxSurf.get_rect().center))
        return boxSurf
    
    def drawReset(self, screenObj):
        screen = screenObj.screen
        textSurf = self.createTextBox("RESET", BLACK, YELLOW, 10, 10)
        screen.blit(textSurf, textSurf.get_rect(center = (100, 50)))

    def drawRandom(self, screenObj):
        screen = screenObj.screen
        textSurf = self.createTextBox("RANDOM", WHITE, PURPLE, 10, 10)
        screen.blit(textSurf, textSurf.get_rect(center = (250, 50)))

    def drawPlayAgain(self, screenObj):
        screen = screenObj.screen
        (X, Y) = screenObj.getScreenSize()
        textSurf = self.createTextBox("PLAY AGAIN", BLACK, GREEN, 10, 10)
        screen.blit(textSurf, textSurf.get_rect(center = (X//2, Y//2-100)))

    def drawQuit(self, screenObj):
        screen = screenObj.screen
        (X, Y) = screenObj.getScreenSize()
        textSurf = self.createTextBox("QUIT", WHITE, RED, 10, 10)
        screen.blit(textSurf, textSurf.get_rect(center = (X-100, 50)))

    def drawRowInput(self, screenObj, inputObj):
        screen = screenObj.screen
        textSurf = self.createTextBox(f'ROW SIZE: {inputObj.rowInput}', BLACK, PINK, 10, 10)
        screen.blit(textSurf, textSurf.get_rect(center = (130, 150)))

    def drawColInput(self, screenObj, inputObj):
        screen = screenObj.screen
        textSurf = self.createTextBox(f'COL SIZE: {inputObj.colInput}', BLACK, PINK, 19, 10)
        screen.blit(textSurf, textSurf.get_rect(center = (130, 200)))

    def drawGenerate(self, screenObj):
        screen = screenObj.screen
        text_surf = self.createTextBox('GENERATE', BLACK, GREEN, 10, 10)
        screen.blit(text_surf, text_surf.get_rect(center = (130, 250)))

    def drawGameOver(self, screenObj):
        screen = screenObj.screen
        (X, Y) = screenObj.getScreenSize()
        font = pygame.font.Font(None, self.fontSize)
        gameOverText = font.render('GAME OVER!', True, RED, BLACK)
        gameOverRect = gameOverText.get_rect()
        gameOverRect.center = (X//2, Y//2-150)
        screen.blit(gameOverText, gameOverRect)

    def drawFinish(self, screenObj):
        screen = screenObj.screen
        (X, Y) = screenObj.getScreenSize()
        font = pygame.font.Font(None, self.fontSize)
        gameOverText = font.render('VICTORY!', True, GREEN, BLACK)
        gameOverRect = gameOverText.get_rect()
        gameOverRect.center = (X//2, Y//2-150)
        screen.blit(gameOverText, gameOverRect)

    def __init__(self):
        self.fontSize = 32
        self.lineLength = 50
        self.lineWidth = 5