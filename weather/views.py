import requests
from django.shortcuts import render
import json
# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=0bc3d85c723add080017a36d65ed56fb'
    city = 'santiago, cl'

    """ciudad = with open('weather/chile.json', 'r') as f:
                ciudades = json.load(f)

    print(ciudades['region'])"""


    r = requests.get(url.format(city)).json()

    city_weather = {
        'city' : city,
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],
    }

    context = {'city_weather' : city_weather}

    return render(request, 'weather/weather.html', context)
