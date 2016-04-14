from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from models import Event

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
    #filters out future events and then filters out past events, leaving only current events, then orders them by status (desc)
    statusQuery = Event.objects.filter(dateStart__lte=datetime.datetime.now()).filter(dateEnd__gte=datetime.datetime.now()).order_by('status')

    if len(statusQuery) == 0:
        context['status'] = Event.NORMAL_STATUS
        context['statusText'] = dict(Event.STATUS_CHOICES)[Event.NORMAL_STATUS]
        context['statusColor'] = dict(Event.STATUS_COLORS)[Event.NORMAL_STATUS]
        context['mostCriticalEvent'] = 0
        context['activeEvents'] = 0
    else:
        context['status'] = statusQuery[0].status
        context['statusText'] = dict(Event.STATUS_CHOICES)[statusQuery[0].status]
        context['statusColor'] = dict(Event.STATUS_COLORS)[statusQuery[0].status]
        context['mostCriticalEvent'] = statusQuery[0].id
        context['activeEvents'] = statusQuery
    return context

# Create your views here.
def index(request):
    context = dict()
    context['currentEvents'] = Event.objects.all()
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
