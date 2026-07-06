import numpy as np


class LogisticRegression:

    def __init__(self, iterations=10000, lr=1):
        self.iterations = iterations
        self.lr = lr
        self.w = None



    # Sigmoid Function
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))


    # Train Model
    def fit(self, X, y):
        m = X.shape[0]
        X = np.hstack((np.ones((m, 1)), X))
        
        #weights
        self.w = np.zeros((X.shape[1], 1))
        
        #gradient Descent
        for _ in range(self.iterations):
            z = X @ self.w
            h = self.sigmoid(z)
            self.w = self.w - self.lr * (1 / m) * X.T @ (h - y)



    def predict(self, X):
        m = X.shape[0]
        X = np.hstack((np.ones((m, 1)), X))
        z = X @ self.w
        h = self.sigmoid(z)
        prediction = []

        for i in h:
            if i >= 0.5:
                prediction.append(1)
            else:
                prediction.append(0)

        return np.array(prediction)

 
    def accuracy(self, y_true, y_pred):
        y_true = y_true.flatten()
        return np.mean(y_true == y_pred)