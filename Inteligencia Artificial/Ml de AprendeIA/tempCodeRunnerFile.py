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
### We select just the column 5
X = boston.data[:,np.newaxis, 5]
print("X data")
print(X)
print(X.ndim)