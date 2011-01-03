from django.conf.urls.defaults import *
from django.views.generic.create_update import create_object

from favoritos.views import index, salvar_favorito
from favoritos.models import Favorito, FavoritoForm

urlpatterns = patterns('',
    (r'^$', index),
    (r'^novo_favorito/$', create_object, {'form_class': FavoritoForm}),
    (r'^salvar_favorito/$', salvar_favorito),
)
