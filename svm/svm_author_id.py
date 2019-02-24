#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]

#########################################################
### your code goes here ###
# Import, create, train and make predictions with the sklearn SVC classifier.
# When creating the classifier, use a linear kernel.
#########################################################

# Import
from sklearn.svm import SVC

# Create with linear kernel
clf = SVC(kernel="rbf", C=10000)

# Train
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

# Predict
t0 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-t0, 3), "s"
ten = pred[10]
print(ten)
twentysix = pred[26]
print(twentysix)
fidy = pred[50]
print(fidy)

# Score
score = clf.score(features_test, labels_test)
print "score:", score

# Accuracy
from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
print "accuracy:", acc
