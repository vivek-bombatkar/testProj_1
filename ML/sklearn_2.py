from sklearn import tree
from sklearn.preprocessing import LabelEncoder
import pandas

data = pandas.read_csv("data.csv",sep=',',names=['age','kids'])

#for label in ['age','kids']:
#    data[label] = LabelEncoder().fit_transform(data[label])
X=data['age']
Y=data['kids']

print X,Y

def getDecisionTreeClassifier():
    return tree.DecisionTreeClassifier()

clf=getDecisionTreeClassifier()
clf=clf.fit(X,Y)

i=31
print ("{0} - {1} : {2}".format("DecisionTreeClassifier", str(i), clf.predict([[i]])))
