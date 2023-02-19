class Rules:
    def isStructured(self, size, levelMatrix):
        row = 2*size[0]-1
        col = 2*size[1]-1
        for i in range(row):
            for j in range(col):
                count = 0
                if(i+1 < row):
                    count += (levelMatrix[i+1][j]==1)
                if(i-1 >= 0):
                    count += (levelMatrix[i-1][j]==1)
                if(j+1 < col):
                    count += (levelMatrix[i][j+1]==1)
                if(j-1 >= 0):
                    count += (levelMatrix[i][j-1]==1)
                if count > 3:
                    return False
        return True
    
    def isValid(self, u, d, l, r, key, screenObj, gameObj, playerObj, guiObj):
        (X, Y) = screenObj.getScreenSize()
        if(key == 119):
            if(playerObj.y_player-guiObj.lineLength < Y//2-guiObj.lineLength//2 or u == 1):
                return False
            return True
        elif(key == 115):
            if(playerObj.y_player+guiObj.lineLength > Y//2-(3*guiObj.lineLength)//2+guiObj.lineLength*gameObj.rowSize or d == 1):
                return False
            return True
        elif(key == 97):
            if(playerObj.x_player-guiObj.lineLength < X//2+guiObj.lineLength//2-guiObj.lineLength//2*gameObj.colSize or l == 1):
                return False
            return True
        elif(key == 100):
            if(playerObj.x_player+guiObj.lineLength > X//2-guiObj.lineLength//2+guiObj.lineLength//2*gameObj.colSize or r == 1):
                return False
            return True
        return False
    
    def isResetClicked(self, pos):
        if(pos[0] > 100-45 and pos[0] < 100+40 and pos[1] > 50-20 and pos[1] < 50+15):
            return True
        return False
    
    def isRandomClicked(self, pos):
        if(pos[0] > 250-58 and pos[0] < 250+58 and pos[1] > 50-20 and pos[1] < 50+15):
            return True
        return False

    def isPlayAgainClicked(self, isGameOver, pos, screenObj):
        (X, Y) = screenObj.getScreenSize()
        if(isGameOver == True and pos[0] > X//2-50-25 and pos[0] < X//2+50+25 and pos[1] > Y//2-100-15 and pos[1] < Y//2-100+15):
            return True
        return False

    def isQuitClicked(self, pos, screenObj):
        (X, Y) = screenObj.getScreenSize()
        if(pos[0] > X-100-35 and pos[0] < X-100+30 and pos[1] > 50-20 and pos[1] < 50+15):
            return True
        return False

    def isRowInputClicked(self, pos):
        if(pos[0] > 100-47 and pos[0] < 150+50 and pos[1] > 150-20 and pos[1] < 150+15):
            return True
        return False

    def isColInputClicked(self, pos):
        if(pos[0] > 100-47 and pos[0] < 150+50 and pos[1] > 200-20 and pos[1] < 200+15):
            return True
        return False

    def isGenerateClicked(self, pos):
        if(pos[0] > 100-38 and pos[0] < 150+45 and pos[1] > 250-18 and pos[1] < 250+12):
            return True
        return False
    
    def __init__(self):
        pass
    
