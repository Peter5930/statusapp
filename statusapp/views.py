from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Event

def paginate(context, request, objectList, itemsPerPage):
    paginator = Paginator(objectList, itemsPerPage)
    page = request.GET.get('page')
    try:
        pageObj = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pageObj = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pageObj = paginator.page(paginator.num_pages)
    context['pageObj'] = pageObj
    context['paginator'] = paginator

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

def db(request):

    return 1

def events(request):
    context = dict()
    context['events'] = Event.objects.all()

    paginate(context, request, Event.objects.all(), 2)

    return render(request, 'events.html', context)

def eventView(request, event_id):
    context = dict()
    context['event'] = Event.objects.get(id=event_id)
    context['scheduleFlagHTML'] = Event.objects.get(id=event_id).scheduleFlagHTML()
    context['statusHTML'] = Event.objects.get(id=event_id).statusHTML()
    context['resolvedHTML'] = Event.objects.get(id=event_id).resolvedHTML()

    paginate(context, request, Event.objects.all(), 1)

    return render(request, 'eventView.html', context)

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
