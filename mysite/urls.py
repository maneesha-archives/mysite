from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #this tells django to also include polls/urls.py
    url(r'^polls/', include('polls.urls', namespace="polls")),
    #add namespace to be able to keep track of multiple projects.
    #This will be used in templates for that project's urls  

    #remember the trailing comma!

    #url takes four arguments:
    #regex to create the url
    #the view that will create the page
    #kwarg -- not covered here
    #name to refer to it unambiguously
)
