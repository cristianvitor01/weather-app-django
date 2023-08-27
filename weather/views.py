import requests
from django.shortcuts import render


def index(request):
    """Return the index.html template"""

    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=8d5c6bf7016c9709a03b9ed452bf8c04'

    city = 'Las Vegas'

    city_weather = requests.get(url.format(city)).json()  # request the API data and convert JSON to Python data types

    print(city_weather)  # temp

    return render(request, 'weather/index.html')
