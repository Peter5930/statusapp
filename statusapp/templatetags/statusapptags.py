from django import template
import json
import datetime
from statusapp.models import Event

register = template.Library()

@register.filter
def get_range( value ):
  """
    Filter - returns a list containing range made from given value
    Usage (in template):

    <ul>{% for i in 3|get_range %}
      <li>{{ i }}. Do something</li>
    {% endfor %}</ul>

    Results with the HTML:
    <ul>
      <li>1. Do something</li>
      <li>2. Do something</li>
      <li>3. Do something</li>
    </ul>

    Instead of 3 one may use the variable set in the views
  """
  return range( 1, value + 1 )

@register.filter()
def updateEvent(event_id):
    # print "updateEvent"
    event = Event.objects.get(id=event_id)
    # print event.dateUpdated
    event.dateUpdated = datetime.datetime.now()
    # print event.dateUpdated
    event.save()
