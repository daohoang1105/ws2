from django.shortcuts import render

from .functionX import testt
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.clickjacking import xframe_options_sameorigin



@xframe_options_exempt
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    a = testt(q)
    try:
        b = a.split("\n")
    except:
        b = [0,0,0,0]
    context = {'b0':b[0],'b1':b[1],'b2':b[2],'b3':b[3],'q':q}
    return render(request, 'home.html', context)

def room(request):
    return render(request, 'room.html')