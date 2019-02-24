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




#########################################################
### your code goes here ###
# Import, create, train and make predictions with the sklearn SVC classifier.
# When creating the classifier, use a linear kernel.
#########################################################

# Import
from sklearn.svm import SVC

# Create with linear kernel
clf = SVC(kernel="linear")

# Train
clf.fit(features_train, labels_train)

# Predict
pred = clf.predict(features_test)
