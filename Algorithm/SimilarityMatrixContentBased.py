"""
    Generate similar item matrix for Content Based Filtering
    @author: Yutthana
"""


import pandas as pd
from scipy import spatial

#read review text & avg rating
f = open('..//Database//Content_output_file500.txt') #from content_based.py
data = []

for line in f:
    line = line.rstrip('\n').split('\t')
    if line[1] == 'rating(avg)':
        line[2] = float(line[2]) # convert str to float
    else:
        line[2] = float(line[2])# convert to int
    data.append(line)

df = pd.DataFrame(data)

#read price
df2 = pd.read_csv('Meta_price.csv', index_col='asin')

#create matrix
data = None
M = df.pivot_table(values=2, index=0, columns=1).fillna(value=0)

#M.to_csv("content_Mat.csv")

#merge
merge_item = pd.merge(M, df2, left_index=True, right_index=True, how='inner').fillna(value=0)

#create table to hold result
result = pd.DataFrame(index=merge_item.index,columns=merge_item.index)

#for each item
for i in range(0,len(merge_item.index)):
    #compare with another item
    for j in range(0,len(merge_item.index)):
        #find cosine similarity of item1 and item2
        result.ix[i,j] = 1-spatial.distance.cosine(merge_item.ix[i,:],merge_item.ix[j,:])

#table to hold the similarity of item
rank = pd.DataFrame(index=result.columns,columns=range(1,11))

#rank data based on cosine similarity
for i in range(0,len(result.columns)):
    rank.ix[i,:10] = result.ix[0:,i].order(ascending=False)[:10].index

#write to file
rank.to_csv('result_content500.csv')
