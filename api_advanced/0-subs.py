#!/usr/bin/python3
"""Script that fetch 10 hot post for a given subreddit."""
import requests

def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for the given subreddit.

    If the subreddit is not found, returns 0 and prints an informative message.

    Args:
        subreddit (str): Name of the subreddit to query.

    Returns:
        int: Number of subscribers, or 0 if an error occurs.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data')
        if data:
            return data.get('subscribers', 0)
        else:
            print(f"Subreddit '{subreddit}' not found.")
            return 0
    else:
        print(f"Error: Unable to retrieve data for subreddit '{subreddit}'.")
        return 0
