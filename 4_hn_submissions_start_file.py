from operator import itemgetter
import json
import requests

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()

submission_dict = []


for submission_id in submission_ids[:10]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {
        
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'info' : 
        
    }
    
    

