from django.shortcuts import render
from django.http import HttpResponse

#An extremely simple view that just returns the content of HttpRepsonse
def index(request):
    return HttpResponse("Hello world. You're at the poll page.")

#some views that take arguments
def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)

    