# Mining_Massive_Dataset

##Features selection for content based

1. `Price of item` – we assume that some item are similar if they have similar price. For example, the Box set of DVD would be more expensive than a single DVD. Also, new movie and popular movie tend to have higher price than old movie and unpopular movie.

2. `Average rating` – we can group this into 2 big category, good and bad movie. The good movie will have high average rating and bad otherwise.

3. `Most frequency words for each movie’s review text` – due to limited of the dataset, the data we have doesn’t contain any information of the movie such as genre, name of actor/actress, year of movie and so on, so we need to extract some information from the review text. We expect to get some information of the movie from review text, such as name of the actor or name of the character in the movie. For example, If Tom Hanks is the actor of the movie, he will be mentioned in the most of review and we will get his name on the list of most frequency words. We use this method to find most frequency word for all of the movie.

##How to run (content-based)

1. Use `read_csv.py` to get meta_data (for price) and review (for reviewerID, review text, asin, rating). Specify number of data here. Ex. 500k reviews.

2. Use `getMostFrequence_Content.py` to get most frequency word lists. Use review file that get from `read_csv.py`. Specify number of reviews here. Ex. > 500 reviews.

3. Use `getSimilar_Content.py` to get similar item matrix. Use output file from `getMostFrequence_Content.py`

##How to run (collaborative filtering)

1. Use `read_csv.py` to get review (for reviewerID, review text, asin, rating). Specify number of data here. Ex. 500k reviews (same as above but we dont need reviewText fro colaborative filtering)

2. Use `getSimilar_CF.py` to get similar matrix. Use review file from `read_csv.py`. Specify number of reviews here. Ex. > 500 reviews.

##Testing

1. Use `UserToItemTable.py` to get user-to-item matrix. Use review file __without review__ text from `read_csv.py`.

2. Use `PrecisionRecall.py` to get precision-recall plot. Use similar matrix file from `content-based(3)` and `colaborative filtering(2)`. Also, use user-to-item matrix from `UserToItemTable.py` to match the item with user. The result will be the plot of Precision vs Recall.
