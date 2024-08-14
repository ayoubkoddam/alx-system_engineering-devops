#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
"""

import requests

def recurse(subreddit, hot_list=None, after="", count=0):
    """Queries the Reddit API and returns a list containing the titles."""
    if hot_list is None:
        hot_list = []

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code >= 400:
            return None

        data = response.json().get('data')
        after = data.get('after')
        count += data.get('dist')

        for c in data.get("children"):
            hot_list.append(c.get("data").get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after, count)

        return hot_list
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None
    except ValueError as e:
        print(f"JSON decode failed: {e}")
        return None
