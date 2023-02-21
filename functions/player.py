from pygame import mixer
import numpy as np
from functions.generators import Generators

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

    def movePlayer(self, key, screenObj, gameObj, guiObj):
        (X, Y) = screenObj.getScreenSize()
        rowSize = gameObj.rowSize
        colSize = gameObj.colSize
        
        j = (self.x_player-(X//2-colSize*guiObj.lineLength//2+guiObj.lineLength//2))//guiObj.lineLength
        i = (self.y_player-(Y//2-guiObj.lineLength//2))//guiObj.lineLength

        mixer.init()
        mixer.music.load('assets/sounds/playermove.wav')
        mixer.music.set_volume(0.2)

        if key == 119:
            if(i-1 < 0 or gameObj.levelMatrix[2*i-1][2*j] == 1):
                return
            self.setPlayer((self.x_player, self.y_player-guiObj.lineLength))
            i -= 1
        elif key == 115:
            if(i+1 >= rowSize or gameObj.levelMatrix[2*i+1][2*j] == 1):
                return
            self.setPlayer((self.x_player, self.y_player+guiObj.lineLength))
            i += 1
        elif key == 97:
            if(j-1 < 0 or gameObj.levelMatrix[2*i][2*j-1] == 1):
                return
            self.setPlayer((self.x_player-guiObj.lineLength, self.y_player))
            j -= 1
        elif key == 100:
            if(j+1 >= colSize or gameObj.levelMatrix[2*i][2*j+1] == 1):
                return
            self.setPlayer((self.x_player+guiObj.lineLength, self.y_player))
            j += 1
        else:
            return

        if(i == rowSize-1 and j == colSize-1):
            gameObj.isGameFinish = True
            mixer.music.load('assets/sounds/victory.mp3')

        if(gameObj.visited[i][j] == 1):
            gameObj.isGameOver = True
            mixer.music.load('assets/sounds/gameover.mp3')
        else:
            gameObj.updateVisited((i, j), 1)
        
        mixer.music.play() 

    def __init__(self, screenObj, gameObj, guiObj):
        (X, Y) = screenObj.getScreenSize()
        colSize = gameObj.colSize
        lineLength = guiObj.lineLength
        x = X//2-colSize*lineLength//2+lineLength//2
        y = Y//2-lineLength//2
        self.setPlayer((x, y))