# Required imports or library dependencies
import re, sys, json

# Is the tweet in English?
# Try and except clause is used
# If try works for english language tweet return true, else false
def isLang(tweet_json, lang = 'en'):
    try:
 	return tweet_json['lang'] == lang
	
    except: return False


# Create a sentiment dictionary
def genSentDict(sent_file):
    sent_file = open(sent_file)
    scores = {}
    
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)        # Convert the score to an integer.        
    
    return scores


# Get a English tweet 
# Check for English Tweets 
# input: tweet as json
# output: tweet terms as list
# unicode encode is used (as suggested in the assignment's given documentation)
# re.findall is used to get the tweet terms/words as list.
def getENTweet(tweet_json):
    if ( isLang(tweet_json) ):
        
	words = tweet_json ['text']
	# unicode to str
	# Reference : https://stackoverflow.com/questions/10288016/usage-of-unicode-and-encode-functions-in-python
	encodeWords = words.encode('utf-8')
        tweet_terms =  re.findall(r'\w+', encodeWords)
        return tweet_terms
    else: return []
    

# Get score from the tweet
# input: tweet as json, sentiment dictionary (hashmap and/or map, python dictionary)
# output: tweet score
def getSentScoreOfTweet(tweet_json, sentDict):
    
    tweet_score = 0
    tweet_terms = getENTweet(tweet_json)

    for term in tweet_terms:
	term = term.lower()
        # tweet_score = tweet_score + sentDict[term]    
        tweet_score = tweet_score + sentDict.get(term,0)

    return tweet_score

# Score the tweets in the tweets file
def getTweetScores(sentDict, tweets_file):
    tweets_file = open(tweets_file)
    sentDict = genSentDict(sentDict)
        
    for tweet in tweets_file:
        tweet_json = json.loads(tweet)
        
        try:
            score = getSentScoreOfTweet(tweet_json, sentDict)
            #print tweet_json['text'],score
            print score

        except: pass


if __name__ == '__main__':
    getTweetScores(sys.argv[1], sys.argv[2])
