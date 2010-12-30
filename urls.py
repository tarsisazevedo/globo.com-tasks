from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

from views import index

admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/docs/', include('django.contrib.admindocs.urls')),
    (r'^$', index),
    (r'^admin/', include(admin.site.urls)),
    (r'^media/(.*)$', 'django.views.static.serve',
           {'document_root': settings.MEDIA_ROOT}),
)
