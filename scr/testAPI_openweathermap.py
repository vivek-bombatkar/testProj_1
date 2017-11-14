
import requests

URL="http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=48a10244f0b2ed7fb4962396eee67c62"

data = requests.get(URL).json()
print(data)