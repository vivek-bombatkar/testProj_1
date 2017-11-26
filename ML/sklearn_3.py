import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
'''
#read data
dataframe = pd.read_fwf('brain.txt')
x_values = dataframe[['Brain']]
y_values = dataframe[['Body']]
'''
data = pd.read_csv("data.csv",sep=',',names=['age','kids'])
#female age
x_values=data[['age']]
#number of kids
y_values=data[['kids']]
#print(X,Y)

#train model on data
body_reg = linear_model.LinearRegression()
body_reg.fit(x_values, y_values)

#visualize results
plt.scatter(x_values, y_values)
plt.plot(x_values, body_reg.predict(x_values))
plt.show()
