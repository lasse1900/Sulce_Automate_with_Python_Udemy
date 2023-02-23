import requests

def get_weather(city, units='metric', api_key='e81ecf86050a97c21b0381f052b5ee2e'):

  url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
  r = requests.get(url)
  
  content = r.json()
  # print(content)

  with open('data.txt', 'w') as file:
    for dicty in content['list']:
      file.write(f"{dicty['dt_txt']}, {dicty['main']['temp']}, {dicty['weather'][0]['description']}\n")

get_weather(city='Washington')