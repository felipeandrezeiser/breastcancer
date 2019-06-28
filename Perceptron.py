from sklearn.neural_network import MLPClassifier



class Perceptron(NeuralNetworks):
    
        def __init__(self, hidden_layer_sizes, learning_rate, regularization_rate, momentum, epochs=200, max_iter = 1000, verbose=False):                  
            super(MLPClassifier, self).__init__(
                hidden_layer_sizes = hidden_layer_sizes, 
                solver = 'lbfgs', 
                activation = 'tanh', 
                warm_start = True, 
                alpha = regularization_rate, 
                learning_rate_init = learning_rate, 
                momentum=momentum,
                max_iter = max_iter,
                tol=0,
                verbose=verbose)
            
            self.epochs=epochs
            self.train_accuracy_curve_ = []
            self.test_accuracy_curve_ = []
        
        def retScoreTrainTest(self, xTrain, yTrain, xTest, yTest):
            return self.score(xTrain, yTrain), self.score(xTest, yTest)
