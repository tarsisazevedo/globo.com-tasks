from django.conf.urls.defaults import *
from django.views.generic.create_update import create_object

from favoritos.views import index, novo_favorito

urlpatterns = patterns('',
    (r'^$', index),
    (r'^novo_favorito/$', novo_favorito),
)
