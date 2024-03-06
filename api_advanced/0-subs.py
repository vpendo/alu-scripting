#!/usr/bin/python3
"""Script that fetches the number of subscribers for a given subreddit."""

import requests


def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for the given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit. Returns 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(
        url, headers=headers, allow_redirects=False
    )  # Split into multiple lines

    if response.status_code == 200:
        data = response.json().get('data')
        if data:
            return data.get('subscribers', 0)
    return 0

# Call the function for testing
print(number_of_subscribers("python"))
