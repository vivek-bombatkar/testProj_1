from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

import pandas

data = pandas.read_csv("data.csv",sep=',',names=['age','kids'])

X=data[['age']]
Y=data[['kids']]

#print(X,Y)

def getDecisionTreeClassifier():
    return tree.DecisionTreeClassifier()

clf=RandomForestClassifier(n_estimators=2).fit(X,Y)

i=37
print ("{0} - {1} : {2}"
       .format("DecisionTreeClassifier", str(i), clf.predict([[i]])))

