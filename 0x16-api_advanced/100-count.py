import requests
from collections import Counter

def count_words(subreddit, word_list, after=None):
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

            # Extract titles from posts
            titles = [post['data']['title'] for post in children]

            # Convert titles to lowercase and concatenate into a single string
            titles_text = ' '.join(titles).lower()

            # Count occurrences of each word in the word_list
            word_counts = Counter(titles_text.split())

            # Print results
            for word in word_list:
                count = word_counts.get(word.lower(), 0)
                if count > 0:
                    print(f"{word.lower()}: {count}")

            # Check if there are more pages
            after = data['data']['after']
            if after is not None:
                # Recursively call the function with the next page
                return count_words(subreddit, word_list, after)

        else:
            return  # Print nothing for invalid subreddit or other errors

    except Exception as e:
        print(f"Error: {e}")

# Example usage
if _name_ == "_main_":
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit_name = sys.argv[1]
        keywords = [x.lower() for x in sys.argv[2].split()]
        count_words(subreddit_name, keywords)