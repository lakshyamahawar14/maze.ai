from functions.rules import Rules

class Player:
    x_player = 0
    y_player = 0

    def getPlayer(self):
        return (self.x_player, self.y_player)
    
    def setPlayer(self, position):
        self.x_player = position[0]
        self.y_player = position[1]

    def resetPlayer(self, size, screenObj, guiObj):
        (X, Y) = screenObj.getScreenSize()
        colSize = size[1]
        lineLength = guiObj.lineLength
        x = X//2-colSize*lineLength//2+lineLength//2
        y = Y//2-lineLength//2
        self.setPlayer((x, y))

    def movePlayer(self, key, screenObj, gameObj, playerObj, guiObj, rulesObj):
        (X, Y) = screenObj.getScreenSize()
        rowSize = gameObj.rowSize
        colSize = gameObj.colSize
        
        j = (self.x_player-(X//2-colSize*guiObj.lineLength//2+guiObj.lineLength//2))//guiObj.lineLength
        i = (self.y_player-(Y//2-guiObj.lineLength//2))//guiObj.lineLength

        u = gameObj.levelMatrix[2*i][j+1]
        d = gameObj.levelMatrix[2*i+2][j+1]
        l = gameObj.levelMatrix[2*i+1][j]
        r = gameObj.levelMatrix[2*i+1][j+1]

        if(rulesObj.isValid(u, d, l, r, key, screenObj, gameObj, playerObj, guiObj) == False):
            return
        gameObj.updateVisited((i, j), 1)
        if(key == 119):
            i -= 1
            self.setPlayer((self.x_player, self.y_player-guiObj.lineLength))
        elif(key == 115):
            i += 1
            self.setPlayer((self.x_player, self.y_player+guiObj.lineLength))
        elif(key == 97):
            j -= 1
            self.setPlayer((self.x_player-guiObj.lineLength, self.y_player))
        elif(key == 100):
            j += 1
            self.setPlayer((self.x_player+guiObj.lineLength, self.y_player))

        if(i == rowSize-1 and j == colSize-1):
            gameObj.isGameFinish = True
        if(gameObj.visited[i][j] == 1):
            gameObj.isGameOver = True

    def __init__(self, screenObj, gameObj, guiObj):
        (X, Y) = screenObj.getScreenSize()
        colSize = gameObj.colSize
        lineLength = guiObj.lineLength
        x = X//2-colSize*lineLength//2+lineLength//2
        y = Y//2-lineLength//2
        self.setPlayer((x, y))