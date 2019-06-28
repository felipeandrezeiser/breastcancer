from sklearn.neural_network import MLPClassifier

from sklearn.metrics import accuracy_score

class NeuralNetworks(MLPClassifier):
    
        # contrutor sem passagem de parâmetros das propriedades para forçar uso dos métodos get e set
        def __init__(self):
            pass
        
        # a class method to create a fit classifier. 
        
        def accuracy(self, X, y):
            pred = self.predict(X)
            n_wrong = np.count_nonzero(pred.ravel() != y.ravel())
            return 1 - n_wrong/len(pred)
        
        def fit(self, X_train, y_train, X_test, y_test):
            
            aux = self.epochs
            print("aux: ", aux)
            for i in range(1, aux + 1):            
                super(MLPClassifier, self).fit(X_train, y_train.ravel())
                if(self.verbose):
                    print('fit ended')
                self.train_accuracy_curve_.append(self.accuracy(X_train, y_train))
                self.test_accuracy_curve_.append(self.accuracy(X_test, y_test))
