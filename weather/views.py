import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def index(request):
    """Return the index.html template"""

    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=8d5c6bf7016c9709a03b9ed452bf8c04'

    cities = City.objects.all()  # return all the cities in the database

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    weather_data = []

    for city in cities:
        city_weather = requests.get(
            url.format(city)).json()  # request the API data and convert JSON to Python data types

        temperature_fahrenheit = city_weather['main']['temp']
        temperature_celsius = fahrenheit_to_celsius(temperature_fahrenheit)
        temperature_fahrenheit_formatado = "{:.1f}".format(temperature_celsius)

        # dict return main data to be passed with context in template.
        weather = {
            'city': city,
            'temperature': temperature_fahrenheit_formatado,
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }

        weather_data.append(weather)  # add the data for the current city into our list

    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'weather/index.html', context)
