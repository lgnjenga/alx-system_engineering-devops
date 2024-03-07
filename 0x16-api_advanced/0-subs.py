import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}  # Set a custom User-Agent to avoid Too Many Requests errors

    try:
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0  # Return 0 for invalid subreddit or other errors

    except Exception as e:
        print(f"Error: {e}")
        return 0

# Example usage
if _name_ == "_main_":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        subscribers = number_of_subscribers(subreddit_name)
        print(subscribers)