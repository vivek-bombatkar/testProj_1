from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pandas

data = pandas.read_csv("data.csv",sep=',',names=['age','kids'])

#for label in ['age','kids']:
#    data[label] = LabelEncoder().fit_transform(data[label])
#print data['age'].values.tolist()

X=[data['age'].values]
Y=data['kids'].values

print X,Y
#exit(0)
#[[30], [33], [28], [35], [30]] ['1kid', '2kid', '1kid', '2kid', '1kid']

def getDecisionTreeClassifier():
    return tree.DecisionTreeClassifier()

clf=RandomForestClassifier(n_estimators=2)
#getDecisionTreeClassifier()
clf=clf.fit(X,Y)

i=31
print ("{0} - {1} : {2}"
       .format("DecisionTreeClassifier", str(i), clf.predict([[i]])))

