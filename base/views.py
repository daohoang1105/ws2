from django.shortcuts import render

from .functionX import testt


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    a = testt(q)
    context = {'a':a}
    return render(request, 'home.html', context)

def room(request):
    return render(request, 'room.html')