import os
import pandas as pd

BASEDIR = os.getcwd()
FILENAME = 'dataset.csv'
FILEPATH = os.path.join(BASEDIR, 'assets', 'datasets', FILENAME)

def insertData(mazeSize, numberOfOnes, difficultyLevel, filepath=FILEPATH):
    df1 = pd.read_csv(filepath)

    df2 = pd.DataFrame({'mazeSize':[mazeSize], 'numberOfOnes':[numberOfOnes], 'difficultyLevel':[difficultyLevel]})
    df1 = pd.concat([df1, df2], ignore_index=True).reset_index(drop=True)

    df1.to_csv(filepath, index=False)