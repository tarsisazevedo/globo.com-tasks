from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.views.generic.simple import direct_to_template

from views import index, cadastrar, meu_delicious_login, meu_delicious_logout

admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/docs/', include('django.contrib.admindocs.urls')),
    (r'^$', index),
    (r'^login/', meu_delicious_login),
    (r'^logout/', meu_delicious_logout),
    (r'^cadastrar/', cadastrar),
    (r'^meu_delicious/', include('favoritos.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^media/(.*)$', 'django.views.static.serve',
           {'document_root': settings.MEDIA_ROOT}),
)