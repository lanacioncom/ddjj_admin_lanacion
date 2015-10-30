from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'admin_ddjj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^api/', include('admin_ddjj_app.urls')),
    url(r'^api/', include('api.urls')),
    # url(r'^$', include(admin.site.urls)),
)
