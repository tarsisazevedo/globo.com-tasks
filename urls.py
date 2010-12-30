from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from django.views.generic.create_update import create_object
from django.contrib.auth.models import User

from views import index, cadastrar, meu_delicious_login, meu_delicious_logout

admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/docs/', include('django.contrib.admindocs.urls')),
    (r'^$', index),
    (r'^accounts/', include('registration.urls')),
    (r'accounts/profile', direct_to_template, {"template": 'profile.html'}),
    (r'^admin/', include(admin.site.urls)),
    (r'^media/(.*)$', 'django.views.static.serve',
           {'document_root': settings.MEDIA_ROOT}),
)
