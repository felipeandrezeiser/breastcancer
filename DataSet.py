import pandas as ped
import numpy as np

from sklearn.cross_validation import train_test_split

class DataSet:
        
        def __init__(self):
            self._x, self._y, self._vlTrainSize, self._vlTestSize, self._xTrain, self._xTest, self._yTrain, self._yTest = [], [], 0, 0, [], [], [], []

        # Usando decorator @property para implementar o método get
        @property
        def x(self):
            return self._x
        
        # método set
        @x.setter
        def x(self, val):
            self._x = val
            
        # Usando decorator @property para implementar o método get
        @property
        def y(self):
            return self._y
        
        # método set
        @y.setter
        def y(self, val):
            self._y = val

        # Usando decorator @property para implementar o método get
        @property
        def vlTrainSize(self):
            return self._vlTrainSize
        
        # método set
        @vlTrainSize.setter
        def vlTrainSize(self, val):
            self._vlTrainSize = val
        
        # Usando decorator @property para implementar o método get
        @property
        def vlTestSize(self):
            return self._vlTestSize
        
        # método set
        @vlTestSize.setter
        def vlTestSize(self, val):
            self._vlTestSize = val
            
        # Usando decorator @property para implementar o método get
        @property
        def xTrain(self):
            return self._xTrain
        
        # método set
        @xTrain.setter
        def xTrain(self, val):
            self._xTrain = val
            
        # Usando decorator @property para implementar o método get
        @property
        def xTest(self):
            return self._xTest
        
        # método set
        @xTest.setter
        def xTest(self, val):
            self._xTest = val
            
        # Usando decorator @property para implementar o método get
        @property
        def yTrain(self):
            return self._yTrain
        
        # método set
        @yTrain.setter
        def yTrain(self, val):
            self._yTrain = val
            
        # Usando decorator @property para implementar o método get
        @property
        def yTest(self):
            return self._yTest
        
        # método set
        @yTest.setter
        def yTest(self, val):
            self._yTest = val
            
        # a class method to create a train test split. 
        @classmethod
        def trainTestSplit(cls, x, y, vlTrainSize, vlTestSize):
            return (train_test_split(x, y, train_size=vlTrainSize, test_size=vlTestSize))
            
        # a class method to create a read CSV. 
        @classmethod
        def readCSV(cls):
            arq = pd.read_csv('/home/fgteixeira/notebookProj/mestrado/primeirosemestre/materias/sistemas adaptativos/breast-cancer.csv', sep=',')
            x = arq.iloc[:,[12,13,14,15,16,17,18,19,20,21]].values  
            y = arq.iloc[:, 1].values
            return(x, y)
