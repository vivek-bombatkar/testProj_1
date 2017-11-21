from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn import tree

'''
X = [[1],[4],[7],[8],[6],[3]]
Y = ['bad','good','good','good','bad','good']
'''
X = [[30],[33],[28],[35],[30],]
Y = ['1kid','2kid','1kid','2kid','1kid']

print X,Y

def getDecisionTreeClassifier():
    return tree.DecisionTreeClassifier()
def getRandomForestClassifier():
    return RandomForestClassifier(n_estimators=2)
def getKNeighborsClassifier():
    return KNeighborsClassifier(n_neighbors=3)
def getLogisticRegression():
    return LogisticRegression()
def getGaussianNB():
    return GaussianNB()

classifier_1 = getDecisionTreeClassifier()
classifier_1 =   classifier_1.fit(X,Y)

classifier_2 = getRandomForestClassifier()
classifier_2 =   classifier_2.fit(X,Y)

classifier_3 = getKNeighborsClassifier()
classifier_3 = classifier_3.fit(X,Y)

classifier_4 = getLogisticRegression()
classifier_4 = classifier_4.fit(X,Y)

classifier_5 = getGaussianNB()
classifier_5 = classifier_5.fit(X,Y)

i=32
print ("{0} - {1} : {2}".format("DecisionTreeClassifier", str(i), classifier_1.predict([[i]])))
print ("{0} - {1} : {2}".format("RandomForestClassifier", str(i), classifier_2.predict([[i]])))
print ("{0} - {1} : {2} ".format("KNeighborsClassifier", str(i), classifier_3.predict([[i]])))
print ("{0} - {1} : {2} ".format("LogisticRegression", str(i), classifier_4.predict([[i]])))
print ("{0} - {1} : {2} \n".format("LogisticRegression", str(i), classifier_5.predict([[i]])))

'''
for i in range(1,10):
    print ("{0} - {1} : {2}".format("DecisionTreeClassifier", str(i), classifier_1.predict([[i]])))
    print ("{0} - {1} : {2}".format("RandomForestClassifier", str(i) ,classifier_2.predict([[i]])))
    print ("{0} - {1} : {2} ".format("KNeighborsClassifier", str(i) ,classifier_3.predict([[i]])))
    print ("{0} - {1} : {2} \n".format("LogisticRegression", str(i) ,classifier_4.predict([[i]])))
    print ("{0} - {1} : {2} \n".format("LogisticRegression", str(i) ,classifier_4.predict([[i]])))

'''