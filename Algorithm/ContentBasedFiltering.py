"""
for Content Based Filtering we retrieve frequently used words from revirew text for frequently purchased items.
@author: Yutthana
"""

import pandas as pd
from pandas import *
from sklearn.feature_extraction.text import TfidfVectorizer

tf = TfidfVectorizer(analyzer='word', min_df = 0, stop_words = 'english')

def f(x):
     return Series(dict(Text = "{%s}" % ', '.join(str(ele) for ele in x['reviewText']),
                        rating = x["overall"].mean()))

#read data from csv
def readcsv(path):
    return pd.read_csv(path, iterator=True, chunksize=10000, skip_blank_lines=True)

#normalize cosine distance item-item
tp = readcsv("..//Database//Movies_and_TV_data_500k_Content.csv")
df = concat(tp, ignore_index=True)

#delete item which has less number of ratings than 500
df = df.groupby("asin").filter(lambda x: len(x) > 500)
df = df.groupby("asin").apply(f)
#df = df.drop(df.columns[[0]], axis=1)
#
##print first asin review text
#print len(df.ix[1,0].split(','))

stopwords = ['"the', "a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]

# Extract the vocabulary of keywords
vocab = dict()
sort_item = []
word_list = []
with open("..//Database//Content_output_file500.txt", 'w') as outfile: #file name that save wordlist
    for i in xrange(len(df)):
        avg_str = '\t'.join([str(df.index[i]), 'rating(avg)', str(df.ix[i,1])])
        avg_str = avg_str + '\n'
        outfile.write(avg_str)
        for text in df.ix[i,0].split(','):
            for term in text.split():
                term = term.lower()
                if len(term) > 2 and term not in stopwords:
                    if vocab.has_key(term):
                        vocab[term] = vocab[term] + 1
                    else:
                        vocab[term] = 1
        # Remove terms whose frequencies are less than a threshold (e.g., 20)
        vocab = {term: freq for term, freq in vocab.items() if freq > 100}
        sort_item = sorted(vocab, key=vocab.__getitem__, reverse=True)[:5]
        ##################
        #write down each word to file (new format)
        for item in sort_item:
            item_str = '\t'.join([str(df.index[i]), item, str(1)])
            item_str = item_str + '\n'
            outfile.write(item_str)
        ##################

        word_list.append(sort_item)
        vocab = dict()
        sort_item = []
