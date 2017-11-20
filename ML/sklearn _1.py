from sklearn.ensemble import RandomForestClassifier
from sklearn import tree

X = [[1],[4],[7],[8],[6],[3]]
Y = ['bad','good','good','good','bad','good']

def getDecisionTreeClassifier():
    return tree.DecisionTreeClassifier()

def getRandomForestClassifier():
    return RandomForestClassifier(n_estimators=2)

classifier_1 = getDecisionTreeClassifier()
classifier_2 = getRandomForestClassifier()
classifier_1 =   classifier_1.fit(X,Y)
classifier_2 =   classifier_2.fit(X,Y)

for i in range(1,10):
    print ("{0} - {1} : {2}".format("DecisionTreeClassifier", str(i), classifier_1.predict([[i]])))
    print ("{0} - {1} : {2}".format("RandomForestClassifier", str(i) ,classifier_2.predict([[i]])))
