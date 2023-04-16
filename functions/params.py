class Params:
    def __init__(self):
        pass

    def getMazeSize(self, gameObj):
        mazeSize = gameObj.mazeSize[0]
        return mazeSize
    
    def getSolutionDistortions(self, solversObj):
        solutionPath = solversObj.solutionPath
        prev1 = solutionPath[0]
        prev2 = solutionPath[1]
        isHorizontal = False
        isVertical = False
        if(prev1[1] == prev2[1]):
            isHorizontal = True
        else:
            isVertical = True
        distortion = 2
        for i in range(2, len(solutionPath)):
            curr = solutionPath[i]
            distortion += 1
            if isHorizontal == True and prev2[1] != curr[1]:
                distortion += 1
                isHorizontal = False
                isVertical = True
            elif isVertical == True and prev2[0] != curr[0]:
                distortion += 1
                isVertical = False
                isHorizontal = True
            prev1 = prev2
            prev2 = curr
        return distortion
    
    def getBranchingFactor(self, gameObj):
        levelMatrix = gameObj.levelMatrix
        row = len(levelMatrix)
        col = len(levelMatrix[0])
        branching_factor = 0
        for i in range(row):
            for j in range(col):
                directions = 0
                if(2*i-1 >= 0 and 2*i-1 < row and 2*j >= 0 and 2*j < col and gameObj.levelMatrix[2*i-1][2*j] == 0):
                    directions += 1
                if(2*i+1 >= 0 and 2*i+1 < row and 2*j >= 0 and 2*j < col and gameObj.levelMatrix[2*i+1][2*j] == 0):
                    directions += 1
                if(2*i >= 0 and 2*i < row and 2*j-1 >= 0 and 2*j-1 < col and gameObj.levelMatrix[2*i][2*j-1] == 0):
                    directions += 1
                if(2*i >= 0 and 2*i < row and 2*j+1 >= 0 and 2*j+1 < col and gameObj.levelMatrix[2*i][2*j+1] == 0):
                    directions += 1
                if(directions > 2):
                    branching_factor += 1

        return branching_factor
    
    def getWallDensity(self, gameObj):
        levelMatrix = gameObj.levelMatrix
        row = len(levelMatrix)
        col = len(levelMatrix[0])
        countOnes = 0
        for i in range(row):
            for j in range(col):
                if levelMatrix[i][j] == 1:
                    countOnes += 1
        density = int((countOnes/(gameObj.rowSize*gameObj.colSize))*100)
        return density
    
    def getMSTCost(self, generatorObj):
        mst = generatorObj.maze
        mstcost = len(mst)
        return mstcost
            




