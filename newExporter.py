import sys
import getopt
import got3
import datetime
import codecs
import csv

def main(argv):
	if len(argv) == 0:
		print 'You must pass some parameters. Use \"-h\" to help.'
		return
		
        filename = "my_tweets.csv"
        tweet_rows = []

	try:
		opts, args = getopt.getopt(argv, "", ("filename=", "username=", "since=", "until=", "querysearch=", "toptweets", "maxtweets="))
		
		tweetCriteria = got3.manager.TweetCriteria()

                tweet_header = []

                tweet_header.append("username")
                tweet_header.append("date")
                tweet_header.append("retweets")
                tweet_header.append("favorites")
                tweet_header.append("text")
                tweet_header.append("geo")
                tweet_header.append("mentions")
                tweet_header.append("hashtags")
                tweet_header.append("id")
                tweet_header.append("permalink")
        
                tweet_rows.append(tweet_header)		

		for opt,arg in opts:
			if opt == '--username':
				tweetCriteria.username = arg
				
			elif opt == '--since':
				tweetCriteria.since = arg
				
			elif opt == '--until':
				tweetCriteria.until = arg
				
			elif opt == '--querysearch':
				tweetCriteria.querySearch = arg
				
			elif opt == '--toptweets':
				tweetCriteria.topTweets = True
				
                        elif opt == '--filename':
                            filename = arg

			elif opt == '--maxtweets':
				tweetCriteria.maxTweets = int(arg)
		
		print 'Searching...\n'
		
		def receiveBuffer(tweets):
			for t in tweets:

                            current_tweet = []
                            
                            current_tweet.append(t.username)
                            current_tweet.append(t.date.strftime(("%Y-%m-%d %H:%M")))
                            current_tweet.append(t.retweets)
                            current_tweet.append(t.favorites) 
    
                            # replace unicode characters with space so it writes to csv
                            t.text = ''.join([i if ord(i) < 128 else ' ' for i in t.text])

                            current_tweet.append(t.text)
                            current_tweet.append(t.geo)
                            current_tweet.append(t.mentions)
                            current_tweet.append(t.hashtags)
                            current_tweet.append(t.id)
                            current_tweet.append(t.permalink)
                            tweet_rows.append(current_tweet)

			print '%d tweet(s) saved on file...\n' % len(tweets)
		
		got3.manager.TweetManager.getTweets(tweetCriteria, receiveBuffer)
		
	except arg:
		print 'Arguments parser error, try -h'
	finally:
                with open(filename, "wb") as f :
                    fileWriter = csv.writer(f, dialect='excel')
                    fileWriter.writerows(tweet_rows)
                    f.close()

		    print 'Done. Tweets stored in ' + filename

if __name__ == '__main__':
	main(sys.argv[1:])
