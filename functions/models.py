import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn import svm
import warnings
warnings.filterwarnings("ignore")

class Models:
    model = None

    def trainModel(self):
        BASEDIR = os.getcwd()
        FILENAME = 'dataset.csv'
        FILEPATH = os.path.join(BASEDIR, 'assets', 'datasets', FILENAME)
        df = pd.read_csv(FILEPATH)
        X = df.drop(['difficultyLevel'], axis=1)
        y = df['difficultyLevel']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=49, shuffle=True)
        SVM = svm.SVC(kernel='linear')
        model = SVM.fit(X_train, y_train)
        return model

    def predictDifficulty(self, x):
        y = self.model.predict([x])
        return y
    
    def __init__(self):
        self.model = self.trainModel()

