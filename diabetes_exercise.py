''' Using the Diabetes dataset that is in scikit-learn, answer the questions below and create a scatterplot
graph with a regression line '''

import matplotlib.pylab as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import datasets

from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

from sklearn.datasets import load_diabetes
diabetes = load_diabetes()

#how many sameples and How many features?
print(diabetes.data.shape)
#442 samples, 10 features!

# What does feature s6 represent?
print(diabetes.DESCR)
#DESCR tells you everything
#S6 = blood sugar levels 


#print out the coefficient
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    diabetes.data, diabetes.target, random_state=11
)

#1. Set up model
mymodel = LinearRegression()

#2. Use fit method to train our model
mymodel.fit(X_train, y_train)
    #x_train is the data, and y_train is the target

#print out the coefficient
print(mymodel.coef_)

#print out intercept
print(mymodel.intercept_)

#3. Use predict to test your model
predicted = mymodel.predict(X_test)
    #predict method doesn't need target cause the goal is to predict the target
#compare with y_test (rename to make it more intuitive)
expected = y_test


#create scatterplot with regression line

plt.plot(expected, predicted, ".")

#dots should be exactly on the line
    #x axis is predicted 
    #y axis is expected 
    #the two should be the same (50,50)
#create 100 points between 0 and 330
x = np.linspace(0,330,100)
print(x)
y = x

plt.plot(x,y)
plt.show()
