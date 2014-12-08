from django.contrib import admin
from polls.models import Choice, Poll

class ChoiceInline(admin.TabularInline):
    #This tells Django: 
    #Choice objects are edited on the Poll admin page. 
    #By default, provide enough fields for 3 choices.
    #(see line added to PollAdmin class below)
    model = Choice
    extra = 3

#This sets the order of the items in the Poll and puts them in sections (aka fieldsets)
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        #first section - no heading, has the field question
        (None, {'fields':['question']}),
        #second section, heading = Date information, has the field pub_date
        ('Date information',{'fields':['pub_date']}),
        #needs a trailing comma
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_recently')

admin.site.register(Poll, PollAdmin)