import requests
import json

# Make an API call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structure of the data.
# descendants = number of comments, kids = ids of people who commented
response_dict = r.json()
readable_file = 'readable_hn_data.json'

with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)
    