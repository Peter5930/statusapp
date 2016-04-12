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
    RESOLVED_COLORS = (
        (RESOLVED, '24A243'),
        (OUTSTANDING, 'ffa500'),
        )
    resolvedFlag = models.IntegerField(choices=RESOLVED_CHOICES, default = OUTSTANDING)
    NORMAL_STATUS = 1
    CRITICAL_STATUS = 2
    STATUS_CHOICES = (
        (NORMAL_STATUS, 'normal'),
        (CRITICAL_STATUS, 'critical'),
        )
    STATUS_COLORS = (
        (NORMAL_STATUS, '24A243'),
        (CRITICAL_STATUS, 'ffa500'),
        )
    status = models.IntegerField(choices=STATUS_CHOICES, default=NORMAL_STATUS)
    UNSCHEDULED = 1
    SCHEDULED = 2
    SCHEDULE_FLAG_CHOICES = (
        (SCHEDULED, 'scheduled'),
        (UNSCHEDULED, 'unscheduled'),
        )
    SCHEDULE_FLAG_COLORS = (
        (SCHEDULED, '24A243'),
        (UNSCHEDULED, 'ffa500'),
        )
    scheduleFlag = models.IntegerField(choices=SCHEDULE_FLAG_CHOICES, default=UNSCHEDULED)

    def __str__(self):
        return self.description

    def list_attributes(self):
        return str(dir(self))

    def scheduleFlagHTML(self):
        htmlString = "<div style='background-color:#"
        count = 0
        while count < len(self.SCHEDULE_FLAG_CHOICES):
            if int(self.scheduleFlag) == int(self.SCHEDULE_FLAG_CHOICES[count][0]):
                htmlString += str(self.SCHEDULE_FLAG_COLORS[count][1])
                htmlString += "'>Event "
                htmlString += str(self.SCHEDULE_FLAG_CHOICES[count][1])
                htmlString += r"</div>"
                return htmlString
            count += 1
        return 'schedule flag error'

    def statusHTML(self):
        htmlString = "<div style='background-color:#"
        count = 0
        while count < len(self.STATUS_CHOICES):
            if int(self.status) == int(self.STATUS_CHOICES[count][0]):
                htmlString += str(self.STATUS_COLORS[count][1])
                htmlString += "'>Status "
                htmlString += str(self.STATUS_CHOICES[count][1])
                htmlString += r"</div>"
                return htmlString
            count += 1
        return 'status error'

    def resolvedHTML(self):
        htmlString = "<div style='background-color:#"
        count = 0
        while count < len(self.RESOLVED_CHOICES):
            if int(self.status) == int(self.RESOLVED_CHOICES[count][0]):
                htmlString += str(self.RESOLVED_COLORS[count][1])
                htmlString += "'>Event "
                htmlString += str(self.RESOLVED_CHOICES[count][1])
                htmlString += r"</div>"
                return htmlString
            count += 1
        return 'error in resolution flag'