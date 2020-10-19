import requests
import json

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}") ## status code of 200 is a successfully get

# Store API response in a variable
response_dict = r.json()
print(f"Total Repositories Returned: {response_dict['total_count']}")


# Explore Each Repository
repo_dict = response_dict['items']
print(f"Total Count of Repo_Dict: {len(repo_dict)}")
print("\n\n")


# Using a for loop, list out the name, owner, stars (stargazers count), url, when created, last updated, and description
for d in repo_dict[:10]:
    name = d["name"]
    owner = d["owner"]["login"]
    stars = d["stargazers_count"]
    r_url = d["html_url"]
    created = d["created_at"]
    updated = d["updated_at"]
    description = d["description"]
    print(f"Repository Name: {name}")
    print(f"Author: {owner}")
    print(f"Number of Stars: {stars}")
    print(f"URL: {r_url}")
    print(f"Date Created: {created}")
    print(f"Last Updated: {updated}")
    print(f"Description: {description}")
    print()


