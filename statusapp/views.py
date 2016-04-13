from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Event

import datetime

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

def getStatus(context, request):
    print "getStatus"
    # q1 = Event.objects.filter(description__startswith='event')
    # print "q1"
    # for i in q1:
    #     print i
    # q2 = Event.objects.filter(dateStart__lte=datetime.datetime.now())#Filters out future events
    # print "q2"
    # for i in q2:
    #     print i
    # q3 = Event.objects.filter(dateEnd__gte=datetime.datetime.now())#Filters out resolved events
    # print "q3"
    # for i in q3:
    #     print i

    #filters out future events and then filters out past events, leaving only current events, then orders them by status (desc)
    statusQuery = Event.objects.filter(dateStart__lte=datetime.datetime.now()).filter(dateEnd__gte=datetime.datetime.now()).order_by('status')
    for i in statusQuery:
        print i
    print type(statusQuery)
    print statusQuery
    print len(statusQuery)

    if len(statusQuery) == 0:
        context['status'] = NORMAL_STATUS
        context['statusText'] = dict(Event.STATUS_CHOICES)[NORMAL_STATUS]
        context['statusColor'] = dict(Event.STATUS_COLORS)[NORMAL_STATUS]
        context['mostCriticalEvent'] = 0
        context['activeEvents'] = 0
    else:
        context['status'] = statusQuery[0].status
        context['statusText'] = dict(Event.STATUS_CHOICES)[statusQuery[0].status]
        context['statusColor'] = dict(Event.STATUS_COLORS)[statusQuery[0].status]
        context['mostCriticalEvent'] = statusQuery[0].id
        context['activeEvents'] = statusQuery

    print "context['status'] = ", context['status']
    print "context['statusText'] = ", context['statusText']
    print "context['statusColor'] = ", context['statusColor']
    print "context['mostCriticalEvent'] = ", context['mostCriticalEvent']

    return context

# Create your views here.
def index(request):
    context = dict()
    getStatus(context, request)
    return render(request, 'index.html', context)

def events(request):
    context = dict()
    context['events'] = Event.objects.all()

    paginate(context, request, Event.objects.all(), 2)
    getStatus(context, request)

    return render(request, 'events.html', context)

def eventView(request, event_id):
    context = dict()
    context['event'] = Event.objects.get(id=event_id)
    context['scheduleFlagHTML'] = Event.objects.get(id=event_id).scheduleFlagHTML()
    context['statusHTML'] = Event.objects.get(id=event_id).statusHTML()
    context['resolvedHTML'] = Event.objects.get(id=event_id).resolvedHTML()

    paginate(context, request, Event.objects.all(), 1)
    getStatus(context, request)

    return render(request, 'eventView.html', context)

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
