#we'll work with the popular adult data set.The data set has been taken from UCI Machine Learning Repository.
#We need to predict if the salary of a given person is less than or more than 50K.
#It is a binary classification problem
#In this data set, the dependent variable is "target."
import pandas as pd
import numpy as np

#load the data
train  = pd.read_csv("C:/Users/I321790/PycharmProjects/Data_Manipulation/train.csv")
test = pd.read_csv("C:/Users/I321790/PycharmProjects/Data_Manipulation/test.csv")

print(train.info())

print("the train data has",train.shape)

#Let have a glimpse of the data set
print(train.head())

nans = train.shape[0] - train.dropna().shape[0]
print ("%d rows have missing values in the train data" %nans)

#only 3 columns have missing values
print(train.isnull().sum())

#Let's count the number of unique values from character variables.
cat = train.select_dtypes(include=['O'])
print(cat.apply(pd.Series.nunique))

#Since missing values are found in all 3 character variables, let's impute these missing values with their respective modes.
train.workclass.value_counts(sort=True)
train.workclass.fillna('Private',inplace=True)

#Occupation
train.occupation.value_counts(sort=True)
train.occupation.fillna('Prof-specialty',inplace=True)


#Native Country
train['native.country'].value_counts(sort=True)
train['native.country'].fillna('United-States',inplace=True)

print(train.isnull().sum())

#Now, we'll check the target variable to investigate if this data is imbalanced or not.
print(train.target.value_counts()/train.shape[0])

#Let's create a cross tab of the target variable with education.
print(pd.crosstab(train.education,train.target,margins=True)/train.shape[0])

#We'll use the famous and formidable scikit learn library
# Scikit learn accepts data in numeric format
# We'll use the labelencoder function.

#load sklearn and encode all object type variables
from sklearn import preprocessing

for x in train.columns:
    if train[x].dtype == 'object':
        lbl=preprocessing.LabelEncoder()
        lbl.fit(list(train[x].values))
        train[x]= lbl.transform(list(train[x].values))

print(train.head())
#<50K = 0 and >50K = 1
print(train.target.value_counts())

# Building a Random Forest Model
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_score
from sklearn.metrics import accuracy_score

y=train['target']
del train['target']

X = train
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=1,stratify=y)

#train the RF classifier
clf = RandomForestClassifier(n_estimators = 500, max_depth = 6)
clf.fit(X_train,y_train)

RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
                max_depth=6, max_features='auto', max_leaf_nodes=None,
                min_impurity_split=1e-07, min_samples_leaf=1,
                min_samples_split=2, min_weight_fraction_leaf=0.0,
                n_estimators=500, n_jobs=1, oob_score=False, random_state=None,
                verbose=0, warm_start=False)
clf.predict(X_test)

#make prediction and check model's accuracy
prediction = clf.predict(X_test)
acc =  accuracy_score(np.array(y_test),prediction)
print ('The accuracy of Random Forest is {}'.format(acc))