__author__ = 'chenghaowei'
from twaiter import TWaiter
import tweepy, sys, twitterparams

# authentication params (supplied via cfn)
consumer_key = twitterparams.OAuthConsKey
consumer_secret = twitterparams.OAuthConsSecret
access_token = twitterparams.OAuthToken
access_token_secret = twitterparams.OAuthTokenSecret

# OAuth via tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def main(term):
    if len(term) == 2:
        search = [term[1]]
    else:
        print "Please provide only one search term. Multi-word terms should be enclosed in quotation marks. Example:  python collector.py kindle fire "
        sys.exit()

    collection = 'tweets'
    waiter = TWaiter(api, collection)
    stream = tweepy.Stream(auth, waiter)

    print "Collecting tweets. Please wait."

    try:
        stream.filter(track=search)
    except Exception, e:
        print "An error occurred. No tweets collected.", e
        stream.disconnect()


if __name__ == '__main__':
    main(sys.argv)