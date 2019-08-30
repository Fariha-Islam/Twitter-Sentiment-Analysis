import matplotlib.pyplot as plt
import operator
import re, sys, json
from collections import Counter
from tweet_sentiment import *

# Input: The downloaded tweets file
# Output: The freq dictionary {key: tweet terms, value: frequency as probability}
def frequency(tweets_file):
    freq = {}
    tweets_file = open(tweets_file)    
    total_words = 0.0

    for tweet in tweets_file:
        tweet_json = json.loads(tweet)
        tweet_terms = getENTweet(tweet_json)
        # Total number of words (terms) in all tweets
        total_words = total_words + len(tweet_terms)
        
        for term in tweet_terms:
            term = term.lower()
            # if the term (key) exist in the freq dict, the value is incremented to keep count of the number of times the term's occured
            # suggested by Ishfaq 
	    try:
               freq[term] += 1
            # new term is added and the value set to 1 for that term (key)  
	    except:
                freq[term] = 1

    # Finds frequency of each term in the file 	
    for term in freq:
	    freq[term] = (freq[term]/(total_words))*1000 # as suggested in the script (multiplied by 1000 to give a larger value)
	    
    return freq

def printFrequency(freqDict):
    for key in freqDict.keys():
        print("%s %.4f" % ( key, freqDict[key] ) ) 

# Plots the 10 most used terms in the twitter data 
# Shared by Ishtiaq! 
def plotFrequencyBar(freqDict):
    lists = sorted(freqDict.items(), key=operator.itemgetter(1), reverse=True)[0:10] 
    terms, counts = zip(*lists)

    r = range(len(terms))

    plt.xticks(r, terms)

    plt.bar(r, counts, align='center')

    plt.show()
           
           
   

if __name__ == '__main__':
    printFrequency(frequency(sys.argv[1]))
    plotFrequencyBar(frequency(sys.argv[1]))
