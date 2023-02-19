class Input:
    isRowInputFocus = True
    isColInputFocus = True

    def takeRowInput(self, key, gameObj):
        if(int(key) < 49 or int(key) > 58):
            return
        gameObj.rowSize = int(key)-48

    def takeColInput(self, key, gameObj):
        if(int(key) < 49 or int(key) > 58):
            return
        gameObj.colSize = int(key)-48

    def toggleRowInputFocus(self):
        if(self.isRowInputFocus == True):
            self.isRowInputFocus = False
        else:
            self.isRowInputFocus = True

    def toggleColInputFocus(self):
        if(self.isColInputFocus == True):
            self.isColInputFocus = False
        else:
            self.isColInputFocus = True

    def __init__(self):
        self.isRowInputFocus = False
        self.isColInputFocus = False