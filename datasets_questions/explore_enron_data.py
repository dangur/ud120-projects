#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat
from feature_format import targetFeatureSplit


enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

# for person in enron_data:
#     print ((person))
# print (enron_data)
# print len(enron_data["SKILLING JEFFREY K"].keys())

# poi = 0
# for person in enron_data:
#     if enron_data[person]["poi"] == 1:
#         poi = poi+1
# print (poi)

# poi_names = open("../final_project/poi_names.txt", "r")
# # print poi_names.read()
# poi = 0
# for name in poi_names:
#     if "(n)" in name or "(y)" in name:
#         print name
#         poi = poi + 1
#
# print poi

# exercised = enron_data["PRENTICE JAMES"]["exercised_stock_options"]
# restrited = enron_data["PRENTICE JAMES"]["restricted_stock"]
# print exercised + restrited

# colwellPoi = enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
# print colwellPoi

# slime_bags = ["SKILLING JEFFREY K", "LAY KENNETH L", "FASTOW ANDREW S"]
#
# for slime_bag in slime_bags:
#     print enron_data[slime_bag]##["total_payments"]


# skilly = enron_data["SKILLING JEFFREY K"]["total_payments"]
# print skilly

# peeps = enron_data.keys()
# salary = 0
# mail = 0
# for peep in peeps:
#     if enron_data[peep]['salary'] != 'NaN':
#         salary = salary + 1
#     if enron_data[peep]['email_address'] != 'NaN':
#         mail = mail + 1
# print salary
# print mail

# peeps = enron_data.keys()
# print len(peeps)
# payments = 0
# for peep in peeps:
#     if enron_data[peep]['total_payments'] == 'NaN':
#         payments = payments + 1
# print payments
# print 100 * float(payments) / float(len(peeps))

feature_list = ["poi", "total_payments"]
data_array = featureFormat(enron_data, feature_list)
label, features = targetFeatureSplit(data_array)

print label
print len(label) + 10
# i = 0
# for lab in label:
#     # print lab
#     if lab == 1.0:
#         print features[i]
#         i = i + 1

#         nada = nada + 1
# totes = len(label)
# percent_losers = 100 * float(nada) / float(totes)
#
# print percent_losers

# print 146 - 21 + 10