from django.db import models
from datetime import datetime
# from django.contrib.contenttypes.models import ContentType

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

    def comment_count(self):
        ct = ContentType.objects.get_for_model(Event)
        obj_pk = self.id
        print "self.id == ", self.id
        return Comment.objects.filter(content_type=ct,object_pk=obj_pk).count()

    def list_attributes(self):
        return str(dir(self))
