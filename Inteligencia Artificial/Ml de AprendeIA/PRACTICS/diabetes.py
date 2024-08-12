import numpy as np
import matplotlib.pyplot as plt

from   sklearn  import linear_model,datasets
diabetes_X,diabetes_y = datasets.load_diabetes(return_X_y=True)


print(f"Before the newaxis: {diabetes_X}") #! I'm just playing with it
print(np.ndim(diabetes_X))
diabetes_X = diabetes_X[:,np.newaxis,2]#* This one allow you, to select the elements of the column2, 
## Selecting the data
diabetes_X_train = diabetes_X[:-20]  #* select all the elements except the last 20 elements
diabetes_X_test = diabetes_X[-20:] #* The opposite, since it's selected from the element of the index -20 increasing to the final of the matrix or set
## selecting the targets

diabetes_y_train = diabetes_y[:-20]  #* select all the elements except the last 20 elements
diabetes_y_test = diabetes_y[-20:] #* The opposite, since it's selected from the element of the index -20 increasing to the final of the matrix or set

## init the model
regr = linear_model.LinearRegression()
## train the model
regr.fit(diabetes_X_train,diabetes_y_train)
## make the predict
diabetes_y_pred = regr.predict(diabetes_X_test)
print(diabetes_y_pred)
