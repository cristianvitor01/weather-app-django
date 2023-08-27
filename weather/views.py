import requests
from django.shortcuts import render


def index(request):
    """Return the index.html template"""

    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=8d5c6bf7016c9709a03b9ed452bf8c04'

    city = 'Las Vegas'

    city_weather = requests.get(url.format(city)).json()  # request the API data and convert JSON to Python data types

    print(city_weather)  # temp

    # dict return main data to be passed with context in template.
    weather = {
        'city': city,
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon']
    }

    context = {'weather': weather}

    return render(request, 'weather/index.html', context)
