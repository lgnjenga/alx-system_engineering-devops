import requests

def recurse(subreddit, hot_list=[], after=None):
    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"

    headers = {'User-Agent': 'Custom User Agent'}  # Set a custom User-Agent to avoid Too Many Requests errors

    try:
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            children = data['data']['children']

            # Append titles to the hot_list
            hot_list.extend([post['data']['title'] for post in children])

            # Check if there are more pages
            after = data['data']['after']
            if after is not None:
                # Recursively call the function with the next page
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list if hot_list else None
        else:
            return None  # Return None for invalid subreddit or other errors

    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
if _name_ == "_main_":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        result = recurse(subreddit_name)
        if result is not None:
            print(len(result))
        else:
            print("None")