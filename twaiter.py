__author__ = 'chenghaowei'
from tweepy import StreamListener
import json, time, sys

class TWaiter(StreamListener):

    # see Tweepy for more info

    def __init__(self, api = None, label = 'default_collection'):
        self.api = api #or API()
        self.counter = 0
        self.label = label
        self.output  = open(label + '.' + time.strftime('%b%d-%H%M') + '.txt', 'w')
        self.deleted  = open('deleted_tweets.txt', 'a')

    def on_data(self, data):
        # The presence of 'in_reply_to_status' indicates a "normal" tweet.
        # The presence of 'delete' indicates a tweet that was deleted after posting.
        if  'in_reply_to_status' in data:
            self.on_status(data)
        elif 'delete' in data:
            delete = json.loads(data)['delete']['status']
            if self.on_delete(delete['id'], delete['user_id']) is False:
                return False


    def on_status(self, status):
        # Get only the text of the tweet and its ID.
        text = str(json.dumps(json.loads(status)['text']))
        id = str(json.dumps(json.loads(status)['id_str']))
        self.output.write("id:" + " " + id[1:-1] + ", " + "text:" + " " + text[1:-1] + "\n")

        self.counter += 1

        # For tutorial purposes, only 500 tweets are collected.
        # Increase this number to get bigger data!
        if self.counter >= 500:
            self.output.close()
            print "Finished collecting tweets."
            sys.exit()
        return

    def on_delete(self, status_id, user_id):
        self.deleted.write(str(status_id) + "\n")
        return

    def on_error(self, status_code):
        sys.stderr.write('Error: ' + str(status_code) + "\n")
        return False