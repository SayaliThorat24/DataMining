"""
    Create User to purchased item table from 1 years purchase history
"""

import pandas as pd
from pandas import *

def readcsv(path):
    return pd.read_csv(path, iterator=True, chunksize=10000, skip_blank_lines=True)

def f(x):
    return Series(dict(Product_ID="{%s}" % ', '.join(str(ele) for ele in x['asin'])))

tp = readcsv("..\\Database\\RecentlyPurchasedItemsByUser.csv")
df = concat(tp, ignore_index=True)

#df = df.groupby("reviewerID").filter(lambda x: len(x) > 500)
df = df.groupby("reviewerID").apply(f)

print len(df)

df.to_csv("..\\Database\\UserToItemTable.csv")