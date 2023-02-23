import requests
# use debugger with a breakpoint at line 9 print(content)

# r = requests.get("https://newsapi.org/v2/everything?qInTitle=united%20states&from=2023-2-21&to=2023-2-22&sortBy=popularity&language=en&apiKey=bc141057a8324cfd9143df3afb4cd7f7")

# content = r.json()

# print(type(content))
# print(content['articles'])

# articles = content['articles']
# print(type(articles))

# for article in articles:
#     print('Title:\n', article['title'], '\nDescription:\n', article['description'])

def get_news(topic, from_date, to_date, language='en', api_key='bc141057a8324cfd9143df3afb4cd7f7'):
    url = f"https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}"
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = [] 
    # print(type(results)) # type is list
    for article in articles:
        results.append(f"Title\n, {article['title']}, '\Description\n', {article['description']}")
    return results

print(get_news(topic='space', from_date='2023-02-21', to_date='2023-02-22'))

