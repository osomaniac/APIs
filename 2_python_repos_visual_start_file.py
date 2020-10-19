import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response_dict = r.json()
repo_dict = response_dict['items']

urls, names, stars = [], [], []
labels = []


# Process results.
# 3 lists - one for links, one for name of project, and one for stars
for d in repo_dict[:10]:
    name = d["name"]
    star = d["stargazers_count"]

    url = d["html_url"]
    hyperlink = f"<a href='{url}'>{name}</a>"

    owner = d["owner"]["login"]
    description = d["description"]
    label = f"{owner}<br />{description}"

    names.append(name)
    stars.append(star)
    urls.append(hyperlink)
    labels.append(label)
    
    




# Make visualization.
data = [{
    'type': 'bar',
    'x': urls,
    'y': stars,
    'hovertext': label,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },

}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
