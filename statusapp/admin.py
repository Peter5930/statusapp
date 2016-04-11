from django.contrib import admin

# Register your models here.
from models import Event#, CustomComment, TestClass, CommentWithTitle

admin.site.register(Event)
# admin.site.register(CustomComment)
# admin.site.register(TestClass)
# admin.site.register(CommentWithTitle)