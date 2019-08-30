# Required imports or library dependencies
import re, sys, json
from tweet_sentiment import *

def gettopTenHashTags(tweets_file, n = 9):
    hashTagFreq = {}
    tweets_file = open(tweets_file)

        
    for tweet in tweets_file:
        
        try: 
           tweet_json = json.loads(tweet)        
        # hashtag entities is being extracted
        # reference : https://dev.twitter.com/overview/api/entities-in-twitter-objects#hashtags
           hashtag = tweet_json['entities']['hashtags']
	
	except: continue 
	#print hashtag
	for htags in hashtag:
            getHashtags = htags['text']
            #print getHashtags
	    # reference : https://stackoverflow.com/questions/15321138/removing-unicode-u2026-like-characters-in-a-string-in-python2-7
            storeHashtag = getHashtags.encode('ascii','ignore')
	    hashTagFreq[storeHashtag] = 1 + hashTagFreq.get(storeHashtag, 0)

    sortedTags = sorted(hashTagFreq,
                        key=hashTagFreq.get,
                        reverse=True)
    
    return sortedTags[0:n]

# Plots the 10 most used hash tags in the twitter data 
# Shared by Ishtiaq! 
def plotHashTagBar(hashTagFreq):
    lists = sorted(hashTagFreq.items(), key=operator.itemgetter(1), reverse=True)[0:10] 
    terms, counts = zip(*lists)

    r = range(len(terms))

    plt.xticks(r, terms)

    plt.bar(r, counts, align='center')

    plt.show()
           
        
if __name__ == '__main__':    
    toptenTags = gettopTenHashTags(sys.argv[1])
    print toptenTags    
    plotHashTagBar(gettopTenHashTags(sys.argv[1]))
    
    
