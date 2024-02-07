
import numpy as np
from sklearn import datasets, linear_model # datasets is the database we're use
import matplotlib.pyplot as plt

# Import the date
boston = datasets.load_boston()
print(boston)
print()

#  Understanding the data

print("Dataset information")
print(boston.keys())
print()