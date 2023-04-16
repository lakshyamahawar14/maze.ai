import os
import pandas as pd

BASEDIR = os.getcwd()
FILENAME = 'dataset.csv'
FILEPATH = os.path.join(BASEDIR, 'assets', 'datasets', FILENAME)

def insertData(paramsObj, gameObj, solversObj, generatorObj, difficultyLevel, filepath=FILEPATH):
    mazeSize = paramsObj.getMazeSize(gameObj)
    wallDensity = paramsObj.getWallDensity(gameObj)
    branchingFactor = paramsObj.getBranchingFactor(gameObj)
    solutionDistortions = paramsObj.getSolutionDistortions(solversObj)
    MSTCost = paramsObj.getMSTCost(generatorObj)
    df1 = pd.read_csv(filepath)

    df2 = pd.DataFrame({'mazeSize':[mazeSize], 'wallDensity':[wallDensity], 'branchingFactor':[branchingFactor], 'solutionDistortions':[solutionDistortions], 'MSTCost':[MSTCost], 'difficultyLevel':[difficultyLevel]})
    df1 = pd.concat([df1, df2], ignore_index=True).reset_index(drop=True)

    df1.to_csv(filepath, index=False)