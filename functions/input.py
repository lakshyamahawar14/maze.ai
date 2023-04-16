class Input:
    isRowInputFocus = True
    isDifficultyInputFocus = True
    rowInput = 0
    difficultyInput = 0

    def takeRowInput(self, key):
        if(int(key) == 8):
            self.rowInput = int(self.rowInput/10)
        elif(int(key) < 48 or int(key) > 57):
            return
        else:
            self.rowInput = self.rowInput*10 + (int(key)-48)

    def takeDifficultyInput(self, key):
        if(int(key) == 8):
            self.difficultyInput = int(self.difficultyInput/10)
        elif(int(key) < 48 or int(key) > 57):
            return
        else:
            self.difficultyInput = self.difficultyInput*10 + (int(key)-48)

    def toggleRowInputFocus(self):
        if(self.isRowInputFocus == True):
            self.isRowInputFocus = False
        else:
            self.isRowInputFocus = True

    def toggleDifficultyInputFocus(self):
        if(self.isDifficultyInputFocus == True):
            self.isDifficultyInputFocus = False
        else:
            self.isDifficultyInputFocus = True

    def __init__(self, gameObj):
        self.isRowInputFocus = False
        self.isDifficultyInputFocus = False
        self.rowInput = gameObj.rowSize
        self.difficultyInput = gameObj.levelNumber