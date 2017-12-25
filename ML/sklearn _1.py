from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
import matplotlib.pyplot as plt
import pandas
from textblob import TextBlob

data = pandas.read_csv("data.csv",sep=',',names=['age','kids'])
#female's age
X=data[['age']]
#number of kids
Y=data[['kids']]
#print(X,Y)

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

def printRes(*args):
    print("{0} says if your age is {1} then you might have {2} kid/s."
          .format(args[0],args[1],args[2]))
#translate using TextBlob
    print( TextBlob("{0} says if your age is {1} then you might have {2} kid/s."
          .format(args[0],args[1],args[2])).translate(to="hi"))

classifier_1 = getDecisionTreeClassifier().fit( X,Y)
classifier_2 = getRandomForestClassifier().fit(X,Y)
classifier_3 = getKNeighborsClassifier().fit(X,Y)
classifier_4 = getLogisticRegression().fit(X,Y)
classifier_5 = getGaussianNB().fit(X,Y)
#new age to predict
i=32
printRes("DecisionTreeClassifier", str(i), classifier_1.predict([[i]]))
printRes("RandomForestClassifier", str(i), classifier_2.predict([[i]]))
printRes("KNeighborsClassifier", str(i), classifier_3.predict([[i]]))
printRes("LogisticRegression", str(i), classifier_4.predict([[i]]))
printRes("GaussianNB", str(i), classifier_5.predict([[i]]))

#visualize results
plt.scatter(X, Y)
plt.plot(X, classifier_5.predict(X))
plt.xlabel("age")
plt.ylabel("kid/s")
plt.show()

'''
Results:
DecisionTreeClassifier कहता है कि आपकी उम्र 32 है तो आपके पास [2] बच्चा / एस हो सकता है
RandomForestClassifier says if your age is 32 then you might have [2] kid/s.
RandomForestClassifier कहते हैं कि आपकी उम्र 32 है, तो आपके पास [2] बच्चा / एस हो सकता है
KNeighborsClassifier says if your age is 32 then you might have [1] kid/s.
KNeighborsClassifier कहते हैं कि अगर आपकी उम्र 32 है तो आपके पास [1] बच्चा / एस हो सकता है
LogisticRegression says if your age is 32 then you might have [1] kid/s.
उपनिवेशवाद का कहना है कि अगर आपकी उम्र 32 है तो आपके पास [1] बच्चे / एस हो सकते हैं
GaussianNB says if your age is 32 then you might have [2] kid/s.
गाऊसीएनबी का कहना है कि अगर आपकी उम्र 32 है तो आपके पास [2] बच्चे / एस हो सकते हैं
'''


