#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers,
for a given subreddit. If an invalid subreddit is given, the function
should return 0.
"""

import requests


def number_of_subscribers(subreddit):
    """Function that queries the Reddit API and returns num of subsribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0

    data = response.json()
    subscribers = data['data']['subscribers']
    return subscribers
