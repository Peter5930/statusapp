from django.shortcuts import render
from django.http import HttpResponse

from .models import Event#, CustomComment, CommentWithTitle

#from statusapp.models import CommentWithTitle
#from statusapp.forms import CommentFormWithTitle

# def get_model():
#     return CommentWithTitle

# def get_form():
#     return CommentFormWithTitle

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

def db(request):

    return 1

def events(request):
    context = dict()
    context['events'] = Event.objects.all()
    #context['comments'] = CustomComment.objects.all()
    #context['commentsWithTitles'] = CommentWithTitle.objects.all()
    return render(request, 'events.html', context)


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)