from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Lets learn Python'},
    {'id': 2, 'name': 'Welcome to Java'},
    {'id': 3, 'name': 'Getting started with JavaScript'},
    {'id': 4, 'name': 'Docker, lets know about it'},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request):
    return render(request, 'base/room.html')
