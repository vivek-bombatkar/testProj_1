import pandas as pd
from pandas.plotting import scatter_matrix

columns = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv('C:\VIVEK\GIT\pandas\data\TEST_DATA_pima-indians-diabetes.data',names=columns)


data.hist()

print(data.boxplot())

print(scatter_matrix(data))