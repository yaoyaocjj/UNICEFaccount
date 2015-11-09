from django.conf.urls import patterns, include, url
from django.contrib import admin
from UNICEF.views import hello

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'UNICEF.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', hello),
    url(r'^admin/', include(admin.site.urls)),
)
