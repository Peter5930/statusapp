from django.contrib import admin

# Register your models here.
from models import Event, CustomComment

admin.site.register(Event)
admin.site.register(CustomComment)