import requests

r = requests.get("http://api.openweathermap.org/data/2.5/forecast?q=Lohja&appid=e81ecf86050a97c21b0381f052b5ee2e&units=metric")

content = r.json()
print(content)

with open('data.txt', 'w') as file:
  for dicty in content['list']:
    file.write(f"{dicty['dt_txt']}, {dicty['main']['temp']}, {dicty['weather'][0]['description']}\n")


