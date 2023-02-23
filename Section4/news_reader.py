import requests

# r = requests.get("https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2023-2-21&to=2023-2-22&sortBy=popularity&language=en&apiKey=bc141057a8324cfd9143df3afb4cd7f7")

# r = requests.get("https://newsapi.org/v2/everything?qInTitle=united%20states&from=2023-2-21&to=2023-2-22&sortBy=popularity&language=en&apiKey=bc141057a8324cfd9143df3afb4cd7f7")

r = requests.get("https://newsapi.org/v2/everything?qInTitle=united%20states&from=2023-2-21&to=2023-2-22&sortBy=popularity&language=en&apiKey=bc141057a8324cfd9143df3afb4cd7f7")

content = r.json()

print(type(content))
print(content['articles'][0]['title'])
print(content['articles'][0]['description'])

