class Input:
    isRowInputFocus = True
    isDifficultyInputFocus = True
    rowInput = 0
    difficultyInput = 0

    def takeRowInput(self, key):
        if(int(key) < 49 or int(key) > 58):
            return
        self.rowInput = int(key)-48

    def takeDifficultyInput(self, key):
        if(int(key) < 49 or int(key) > 53):
            return
        self.difficultyInput = int(key)-48

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