import numpy as np
from classification import LogisticRegression

X = np.array([
    [0,0,0,0],
    [0,0,0,1],
    [0,0,1,0],
    [0,0,1,1],
    [0,1,0,0],
    [0,1,0,1],
    [0,1,1,0],
    [0,1,1,1],
    [1,0,0,0],
    [1,0,0,1],
    [1,0,1,0],
    [1,0,1,1],
    [1,1,0,0],
    [1,1,0,1],
    [1,1,1,0],
    [1,1,1,1]
])

y = np.array([
    [0],
    [1],
    [1],
    [0],
    [1],
    [0],
    [0],
    [1],
    [1],
    [0],
    [0],
    [1],
    [0],
    [1],
    [1],
    [0]
])

#create the model
model = LogisticRegression(
    iterations=10000,
    lr=1
)

#train model
model.fit(X, y)

#predict
prediction = model.predict(X)


print("Actual Output:")
print(y.flatten())
print("\nPredicted Output:")
print(prediction)
print("\nAccuracy:", model.accuracy(y, prediction))