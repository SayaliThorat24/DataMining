"""
    For Collaborative Filtering we require similar item matrix.
    In this code we retrieve most frequently purchased items and build item to item similarity matrix based on cosine distance.
"""

import pandas as pd
from pandas import *
from scipy import spatial
import numpy as np

#read data from csv
def readcsv(path):
    return pd.read_csv(path, iterator=True, chunksize=10000, skip_blank_lines=True)

#normalize cosine distance item-item
tp = readcsv("..\\Database\\Movies_and_TV_data_500k_Collaborative.csv")
df = concat(tp, ignore_index=True)

#delete item which has less number of ratings than 500
df = df.groupby("asin").filter(lambda x: len(x) > 500)

#create utility matrix
table = df.pivot_table(values='overall', index=['reviewerID'], columns=['asin'])

#normalize data
table = table.apply(lambda x: (x - np.mean(x)))

#fill emptyspace with 0
table = table.fillna(value=0)

#create table to hold result
result = pd.DataFrame(index=table.columns,columns=table.columns)


 #for each item
for i in range(0,len(result.columns)):
    #compare with another item
    for j in range(0,len(result.columns)): 
        #find cosine similarity of item1 and item2
        result.ix[i,j] = 1-spatial.distance.cosine(table.ix[:,i],table.ix[:,j])

#table to hold the similarity of item
rank = pd.DataFrame(index=result.columns,columns=range(1,11))

#rank data based on cosine similarity
for i in range(0,len(result.columns)):
    rank.ix[i,:10] = result.ix[0:,i].order(ascending=False)[:10].index

#write to file
rank.to_csv('..\\Database\\Item_Similarity_Matrix_500_Collaborative.csv')