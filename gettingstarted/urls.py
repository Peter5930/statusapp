from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import statusapp.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', statusapp.views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^events/$', statusapp.views.events, name='events'),
    url(r'^events/(?P<event_id>[0-9]+)/$', statusapp.views.eventView, name='detail'),
    #url(r'^events/(?P<event_id>[0-9]+)/(?P<comment_id>[0-9]+)/$', statusapp.views.commentUpdate, name='commentUpdate'),
]
