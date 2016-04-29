"""
    Data set which we are using contains many field which are not required for Recommendation Algorithm.
    This code helps to retrieve 80% of data with required fields for both Content Based and Collaborative Filtering.
"""

import gzip
import csv

def parsecsv(path):
    outputFile = open("..//Database//Meta_price.csv", 'wb')  # save file name
    unusedKey = ['title', 'imUrl', 'related', 'salesRank', 'brand', 'categories', 'description']  # for meta file
    #outputFile = open("..\\Database\\Movies_and_TV_data_500k_Content.csv", 'wb')#For Content Based Filtering
    #outputFile = open("..\\Database\\Movies_and_TV_data_500k_Collaborative.csv", 'wb') # For Collaborative Filtering
    #unusedKey = ['reviewerID', 'helpful', 'reviewerName', 'summary', 'unixReviewTime']  # for Content Based Filtering
    #unusedKey = ['reviewTime', 'helpful', 'reviewerName', 'summary', 'unixReviewTime', 'reviewText'] #for Collaborative Filtering
    dataFile = gzip.open(path, 'r')
    count = 1
    for row in dataFile:
        data = eval(row)
        for key in unusedKey:
            if key in data:
                del data[key]
        if count == 1:
            w = csv.DictWriter(outputFile, data.keys())
            w.writeheader()
            count += 1
        w.writerow(data)
        count += 1
        # chunk size (approx. 80% of data)
        count += 1
        if count == 450000:
            break
        # write data
        w.writerow(data)
    outputFile.close()
    print "Total no of records: " + str(count)

#parsecsv("..\\Database\\reviews_Movies_and_TV.json.gz")
parsecsv("..\\Database\\meta_Movies_and_TV.json.gz")