from django.shortcuts import render_to_response
from django.template import RequestContext

from favoritos.models import Favorito

def index(request):
    favoritos = Favorito.objects.all()
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))
