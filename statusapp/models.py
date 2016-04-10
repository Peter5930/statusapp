from django.db import models
from datetime import datetime
from django_comments.models import CommentAbstractModel

# Create your models here.
class Event(models.Model):
    description = models.CharField(max_length=256, default="")
    dateStart = models.DateTimeField('event start date', auto_now_add=False)
    dateEnd = models.DateTimeField('event end date', auto_now_add=False)
    dateUpdated = models.DateTimeField('event updated date', default=datetime.now())
    RESOLVED = 1
    OUTSTANDING = 2
    RESOLVED_CHOICES = (
        (RESOLVED, 'resolved'),
        (OUTSTANDING, 'outstanding')
        )
    resolvedFlag = models.IntegerField(choices=RESOLVED_CHOICES, default = OUTSTANDING)
    NORMAL_STATUS = 1
    CRITICAL_STATUS = 2
    STATUS_CHOICES = (
        (NORMAL_STATUS, 'normal'),
        (CRITICAL_STATUS, 'critical'),
        )
    status = models.IntegerField(choices=STATUS_CHOICES, default=NORMAL_STATUS)

    def __str__(self):
        return self.description

class CustomComment(CommentAbstractModel):
    event = models.ForeignKey(Event)