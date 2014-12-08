from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from polls.models import Poll 

#An extremely simple view that just returns the content of HttpRepsonse
#def index(request):
#    return HttpResponse("Hello world. You're at the poll page.")


#A view that actually does something
#Displays latest 5 poll questions separated by commas (by date)
def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    #Like this,page is hard coded in the view.  Better to have html template
    # output = ", ".join([p.question for p in latest_poll_list])
    # return HttpResponse(output)
    template = loader.get_template('polls/index.html')
    #context = RequestContext(request, {'latest_poll_list':latest_poll_list})
    #return HttpResponse(template.render(context))
    #Below two lines are same as above two lines
    context = {'latest_poll_list':latest_poll_list}
    return render(request, 'polls/index.html', context)


#some views that take arguments
def detail(request, poll_id):
    #return HttpResponse("You're looking at poll %s." % poll_id)
    #Add 404 the hard way
    # try:
    #     poll = Poll.objects.get(pk=poll_id)
    # except:
    #     raise Http404
    # return render(request, 'polls/detail.html', {'poll':poll})
    # Add 404 handling the easy way
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll':poll})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)

