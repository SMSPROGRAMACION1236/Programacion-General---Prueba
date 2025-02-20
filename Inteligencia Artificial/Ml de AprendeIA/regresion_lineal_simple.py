# we import the libraries that we'll use
"""Numpy, we're going to use because we need to work with numerical information"""
import numpy as np
from sklearn import datasets, linear_model # datasets is the database we're use
import matplotlib.pyplot as plt


# Import the data
"""This dataset, calling boston, we're going to use to train the model"""
boston = datasets.load_boston()
print(boston)
print()

#  Understanding the data

print("Dataset information")
print(boston.keys()) # the information  of the dataset
print()

## To check the features of the dataset
print("features of the dataset")
print(boston.DESCR)

# To check the quantities of data

print("Quantities of Data")
print(boston.data.shape)

# To know the columns labels and its information
print("Columns names")
print(boston.feature_names)

## We prepare the data to do the linear regression
### We select just the column 6
X = boston.data[:,np.newaxis, 5]
print("X data")
print(X)
print(X.ndim)

### We define the data to the labels
y = boston.target
print("Y Data")
print(y)
## We put graphic of the data maybe using matplotlib
plt.scatter(X, y)
plt.xlabel("Numbers of rooms")
plt.ylabel("Price medium")
# print(plt.show())

## We import the modules to use with the training

from sklearn.model_selection import train_test_split
## We put the data in train and test

X_train, X_test,y_train, y_test = train_test_split(X, y, test_size=0.2) # 0.2 is like the 20% of the data
# We choose the algorithm that we'll use
lr  = linear_model.LinearRegression()
#we train the model
lr.fit(X_train,y_train)
# we do the prediction with the testing data
Y_pred = lr.predict(X_test)
print(Y_pred)
print(y_test)

## we make a graphic using matplotlib

plt.scatter(X_test, y_test)
plt.plot(X_test, Y_pred , color='red', linewidth = 3)
plt.title("Simple Lineal Regression")
plt.xlabel("Numbers of People")
plt.ylabel("Medium Level")
print(plt.show())

print()
# Calculate the "A"
print("Data of the model")
print()
print("Value of the quotient 'a'")
print(lr.coef_)
#Calculate the "B" Value
print("The value of the quotient 'b'")
print(lr.intercept_)


# We build the equation
print("The equation of the model is a: ")
print("y= ", lr.coef_, "x", lr.intercept_)

# We calculate the r(2)

print()
print("The precision of the model")
print(lr.score(X_train, y_train)) # The result is bud because this algorithm is not good for this data, there are better models to apply
