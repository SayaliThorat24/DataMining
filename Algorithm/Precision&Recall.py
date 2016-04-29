"""
    In this code we are calculating how precise our prediction is. This we are judging on values of Precision and Recall.
    For this calculation we are hiding 40% of items for test users. Use this testing set to test collaborative and content based filtering.
    Use result data to calculate precision and recall.
"""

import random

f = open('..//Database//UserToItemTable.csv') #from UserToItemTable.py
all_item = []
hide_item = []
y_true = []

for item in f:
    item = item.replace('{', '').replace('}', '').replace('"', '').replace(' ', '')
    item = item.rstrip().split(',')
    all_item.append(item)
    y_true.append(item[1:])
    random_item = random.sample(item[1:], int(round((len(item)*0.6) - 0.5))) #hide 40% of data
    hide_item.append(random_item)

sim = open('Movie_500_result.csv') #For Collaborative Filtering
#sim = open('result_content500.csv') #For Content Based Filtering
sim_item = []
sim_key = []
k = 4 #number of k

#read similar item from file and append in list
for item in sim:
    item = item.rstrip().split(',')
    sim_key.append(item[0])
    sim_item.append(item[1:k+2])

del y_true[0]
#set up y pred
y_pred = []
for i in xrange(1, len(hide_item)):
    recommend_item = []
    for j in hide_item[i]:
        if j in sim_key:
            recommend_item = recommend_item + sim_item[sim_key.index(j)][1:]
    y_pred.append(recommend_item)


precision_score = []
recall_score = []
total_recall = 0.0
total_precision = 0.0

##calculate precision & recall
for i in xrange(len(y_true)):
    if len(y_pred[i]) == 0:
        precision_score.append(0.0)
        recall_score.append(0.0)
    else:
        tp = len(list(set(y_true[i]) & set(y_pred[i])))
        precision = float(tp)/float(len(y_pred[i]))
        recall = float(tp)/float(len(y_true[i]))
        precision_score.append(precision)
        total_precision += precision
        total_recall += recall

print total_precision
print total_recall