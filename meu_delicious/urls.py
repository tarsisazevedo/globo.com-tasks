from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from django.views.generic.date_based import archive_index

from views import cadastrar
from favoritos.models import Favorito

admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/docs/', include('django.contrib.admindocs.urls')),
    (r'^$', archive_index, {"queryset": Favorito.objects.order_by('-data'), 
                            'date_field': 'data', 
                            "template_name": 'index.html', 
                            'template_object_name': 'favoritos',}),
    (r'^login/', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^logout/', 'django.contrib.auth.views.logout', {'template_name': 'logout.html', 'next_page': '/'}),
    (r'^cadastrar/', cadastrar),
    (r'^meu_delicious/', include('favoritos.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^media/(.*)$', 'django.views.static.serve',
           {'document_root': settings.MEDIA_ROOT}),
)
