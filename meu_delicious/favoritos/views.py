from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse 

from favoritos.models import Favorito, FavoritoForm

def index(request):
    favoritos = Favorito.objects.filter(user=request.user)
    return render_to_response("profile.html", locals(), context_instance=RequestContext(request))

def salvar_favorito(request):
    import ipdb;ipdb.set_trace()
    if request.method == "POST":
        titulo = request.POST['titulo']
        url = request.POST['url']
        user = request.user

        favorito = Favorito.objects.create(titulo=titulo, url=url, user=user)
        favorito_form = FavoritoForm(instance=favorito)
        if favorito_form.is_valid():
            favorito.save()
            return HttpResponseRedirect('/meu_delicious')
        else:
            return HttpResponseRedirect('/meu_delicious/novo_favorito')
    
    
