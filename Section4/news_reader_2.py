import requests
# use debugger with a breakpoint at line 9 print(content)
# https://squatsstreak.medium.com/guide-to-use-news-api-in-5-minutes-for-free-23d66302dc41

r = requests.get("https://newsapi.org/v2/everything?qInTitle=united%20states&from=2023-2-21&to=2023-2-22&sortBy=popularity&language=en&apiKey=bc141057a8324cfd9143df3afb4cd7f7")

content = r.json()

print(type(content))
print(content['articles'])
# print(content['articles'][1]['title']['content']['url'])
# print(content['articles'][0]['title'])
# print(content['articles'][0]['description'])

articles = content['articles']
print(type(articles))

for article in articles:
    print('Title:\n', article['title'], '\nDescription:\n', article['description'])