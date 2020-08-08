import requests
from django.shortcuts import render
from bs4 import BeautifulSoup

# Create your views here.


def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get('search')
    print(search)
    front_end = {
        'search': search,
    }
    return render(request, 'CraigsApp/new_search.html', front_end)

