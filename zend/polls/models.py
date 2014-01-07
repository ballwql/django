import datetime
from django.utils import timezone
from django.db import models

class Poll(models.Model):
    pub_date=models.DateTimeField('date publish')
    question=models.CharField(max_length=200)    
    def __unicode__(self): #import for own sanity but also because objects'representations-admin 
        return self.question
    def was_published_recently(self):
        return self.pub_date>=timezone.now()-datetime.timedelta(days=1)
    was_published_recently.admin_order_field='pub_date'
    was_published_recently.boolean=True
    was_published_recently.short_description='Published recently?'
    
class Choice(models.Model):
    poll=models.ForeignKey(Poll)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __unicode__(self):
        return self.choice_text
    
    
 