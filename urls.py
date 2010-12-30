from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

from views import index

urlpatterns = patterns('',
    # Example:
    # (r'^meu_delicious/', include('meu_delicious.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/docs/', include('django.contrib.admindocs.urls')),
    (r'^$', index),
    (r'^admin/', include(admin.site.urls)),
)
