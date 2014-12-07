from django.contrib import admin
from polls.models import Poll

#This sets the order of the items in the Poll
class PollAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question']

admin.site.register(Poll, PollAdmin)