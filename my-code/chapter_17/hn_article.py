import requests
import json
# Make an API call, and store the response.
url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Convert the response object to a dictionary.
response_dict = r.json()

# Process results.
response_string = json.dumps(response_dict, indent=4)
print(response_string)