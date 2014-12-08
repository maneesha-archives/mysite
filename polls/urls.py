from django.conf.urls import patterns, url
from polls import views


#mysite/urls.py includes a line that says to include this file
urlpatterns = patterns('',
    url(r'^$', views.index, name='index')

    #url takes four arguments:
    #regex to create the url 
    #the view that will create the page
    #kwarg -- not covered here
    #name to refer to it unambiguously
    )

