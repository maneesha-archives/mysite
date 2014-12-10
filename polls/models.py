from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    #this along with list_filter in admin.py creates option to filter by date

    def __unicode__(self):
        return u'%s %s' %(self.question, self.pub_date)


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    
    def __unicode__(self):
        return u'%s %s' % (self.choice, self.votes)

