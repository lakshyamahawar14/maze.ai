import os
import pandas as pd

BASEDIR = os.getcwd()
FILENAME = 'dataset.csv'
FILEPATH = os.path.join(BASEDIR, 'assets', 'datasets', FILENAME)

def insertData(rowSize, colSize, numberOfSolutions, numberOfOnes, solutionsPerPath, difficultyLevel, filepath=FILEPATH):
    df1 = pd.read_csv(filepath)

    df2 = pd.DataFrame({'rowSize':[rowSize], 'colSize':[colSize], 'numberOfSolutions':[numberOfSolutions],'numberOfOnes':[numberOfOnes], 'solutionsPerPath':[solutionsPerPath], 'difficultyLevel':[difficultyLevel]})
    df1 = pd.concat([df1, df2], ignore_index=True).reset_index(drop=True)

    df1.to_csv(filepath, index=False)