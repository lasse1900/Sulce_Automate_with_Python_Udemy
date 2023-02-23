import requests


def get_news(country, api_key='bc141057a8324cfd9143df3afb4cd7f7'):
  url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
  r = requests.get(url)
  content = r.json()
  articles = content['articles']
  results = []
  for article in articles:
    results.append(f"TITLE\n'{article['title']}, '\nDESCRIPTION\n', {article['description']}")
  return results

print(get_news(country='fi'))