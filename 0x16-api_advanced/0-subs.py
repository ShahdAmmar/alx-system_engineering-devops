#!/usr/bin/python3
""" Module that returns the number of subscribers for a given subreddit """
import requests


def number_of_subscribers(subreddit):
    """ This functions returns the total number
            of subscribers for a given subreddit.
    Args:
        subreddit: name of the subreddit
    Return:
        No. subscribers for a given subreddit or 0 if invalid subreddit
    """
    headers = {'User-Agent': 'My-User-Agent'}
    response = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json",
                            headers=headers,
                            allow_redirects=False)
    if response.status_code > 299:
        return 0

    subreddit = response.json()
    no_subscribers = subreddit.get('data').get('subscribers')
    return no_subscribers
