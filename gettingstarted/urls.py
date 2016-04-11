from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import statusapp.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', statusapp.views.index, name='index'),
    url(r'^db', statusapp.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^events', statusapp.views.events, name='events'),
]
