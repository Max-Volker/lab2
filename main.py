import requests


city = "Moscow,RU"
appid = "876828f9f641c1a8fb906839e5143749"

res = requests.get("http://api.openweathermap.org/data/2.5/weather",
params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на сутки:")
print("Город", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Скорость ветра",data["wind"]["speed"])
print("Видимость",data["visibility"])