from django.contrib import admin
from polls.models import Poll

#This sets the order of the items in the Poll and puts them in sections (aka fieldsets)
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        #first section - no heading, has the field question
        (None, {'fields':['question']}),
        #second section, heading = Date information, has the field pub_date
        ('Date information',{'fields':['pub_date']}),
        #needs a trailing comma
    ]

admin.site.register(Poll, PollAdmin)