from django.shortcuts import render


def index(request):
    """Return the index.html template"""
    return render(request, 'weather/index.html')
