from django.shortcuts import render
from django.http import HttpResponse

from .models import Event, CustomComment

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def db(request):

    return 1

