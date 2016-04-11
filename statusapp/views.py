from django.shortcuts import render
from django.http import HttpResponse

from .models import Event

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

def db(request):

    return 1

def events(request):
    context = dict()
    context['events'] = Event.objects.all()
    return render(request, 'events.html', context)

def eventView(request, event_id):
    context = dict()
    context['event'] = Event.objects.get(id=event_id)
    return render(request, 'eventView.html', context)

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)