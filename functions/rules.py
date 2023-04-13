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
    
    def isResetClicked(self, pos):
        if(pos[0] > 100-44 and pos[0] < 100+40 and pos[1] > 50-20 and pos[1] < 50+15):
            return True
        return False
    
    def isRandomClicked(self, pos):
        if(pos[0] > 250-58 and pos[0] < 250+58 and pos[1] > 50-20 and pos[1] < 50+15):
            return True
        return False

    def isPlayAgainClicked(self, isGameOver, pos, screenObj):
        (X, Y) = screenObj.getScreenSize()
        if(isGameOver == True and pos[0] > X//2-50-25 and pos[0] < X//2+50+25 and pos[1] > Y//2-100-15-100 and pos[1] < Y//2-100+15-100):
            return True
        return False

    def isQuitClicked(self, pos, screenObj):
        (X, Y) = screenObj.getScreenSize()
        if(pos[0] > X-100-35 and pos[0] < X-100+30 and pos[1] > 50-20 and pos[1] < 50+15):
            return True
        return False

    def isRowInputClicked(self, pos):
        if(pos[0] > 100-49 and pos[0] < 150+52 and pos[1] > 150-20 and pos[1] < 150+15):
            return True
        return False

    def isGenerateClicked(self, pos):
        if(pos[0] > 100-39 and pos[0] < 150+46 and pos[1] > 250-19-50 and pos[1] < 250+16-50):
            return True
        return False
    
    def isDifficultyInputClicked(self, pos, screenObj):
        (X, Y) = screenObj.getScreenSize()
        if(pos[0] > 100-57 and pos[0] < 150+65 and pos[1] > Y-100-20 and pos[1] < Y-100+18):
            return True
        return False
    
    def isRateClicked(self, pos, screenObj):
        (X, Y) = screenObj.getScreenSize()
        if(pos[0] > 100-35 and pos[0] < 150+25 and pos[1] > Y-50-20 and pos[1] < Y-50+18):
            return True
        return False
    
    def __init__(self):
        pass
    
