# DataMining

#Item-to-Item Colaborative Filltering

read_csv.py - Read data from "reviews_Amazon_Instant_Video.json.gz"(approx. 80%) then delete unused key, and write to the csv file. Keys used in this project are ['ReviewerID', 'asin', 'overall']. 

*asin - item id

*overall - rating

item_to_item_CF.py - Read csv file that get from read_csv.py then put the movie with more than 500 reviews from user into dataframe. Transform dataframe to utility matrix then normalize the data and compute the cosine similarity. Rank the top 10 highest similarity, then write to the output file.

instance_result_Normcosine_500.csv - Result of the top 10 similar movies.

** reviews_Amazon_Instant_Video.json.gz can be downloaded from http://jmcauley.ucsd.edu/data/amazon/links.html
