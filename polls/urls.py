from django.conf.urls import patterns, url
from polls import views


#mysite/urls.py includes a line that says to include this file
urlpatterns = patterns('',
    #ex: /polls/
    url(r'^$', views.index, name='index'),

    #ex: /polls/5/
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),

    #ex: polls/5/results/
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),

    #ex: polls/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),

    #url takes four arguments:
    #regex to create the url 
    #the view that will create the page
    #kwarg -- not covered here
    #name to refer to it unambiguously
    )

