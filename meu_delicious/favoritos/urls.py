from django.conf.urls.defaults import *
from django.views.generic.create_update import create_object

from favoritos.views import index, salvar_favorito
from favoritos.models import Favorito

urlpatterns = patterns('',
    (r'^$', index),
    (r'^novo_favorito/$', create_object, {'model': Favorito}),
    (r'^salvar_favorito/$', salvar_favorito),
)
