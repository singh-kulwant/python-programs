#!/usr/bin/python -tt
from twython import Twython
from twython import TwythonStreamer
import csv
import json
import pandas as pd


def showTweets():
    print('Creating connection')
    with open("twitter_credentials.json", "r") as file:
        creds = json.load(file)

    python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

    # Create our query
    query = {'q': 'data science',
             'result_type': 'popular',
             'count': 10,
             'lang': 'en',
             }

    print('reading tweets')
    # Search tweets
    dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}
    for status in python_tweets.search(**query)['statuses']:
        dict_['user'].append(status['user']['screen_name'])
        dict_['date'].append(status['created_at'])
        dict_['text'].append(status['text'])
        dict_['favorite_count'].append(status['favorite_count'])

    # Structure data in a pandas DataFrame for easier manipulation
    df = pd.DataFrame(dict_)
    df.sort_values(by='favorite_count', inplace=True, ascending=False)
    df.head(5)
    print(df)


# Define a main() function that prints a little greeting.
def main():
    showTweets()


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
