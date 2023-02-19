class Input:
    isRowInputFocus = True
    isColInputFocus = True
    rowInput = 0
    colInput = 0

    def takeRowInput(self, key):
        if(int(key) < 49 or int(key) > 58):
            return
        self.rowInput = int(key)-48

    def takeColInput(self, key):
        if(int(key) < 49 or int(key) > 58):
            return
        self.colInput = int(key)-48

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

    def __init__(self, gameObj):
        self.isRowInputFocus = False
        self.isColInputFocus = False
        self.rowInput = gameObj.rowSize
        self.colInput = gameObj.colSize