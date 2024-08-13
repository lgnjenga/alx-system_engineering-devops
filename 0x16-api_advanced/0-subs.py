#!/usr/bin/python3
"""
    A function that queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a
    given subreddit. If an invalid subreddit is given,
    the function should return 0.
"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    '''
        Return total number of subscribers on a given subreddit."
    '''
    user_agent = {'User-Agent': 'Mozilla/5.0'}
    url = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit), headers=user_agent).json()
    try:
        return url.get('data').get('subscribers')
    except Exception:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])
