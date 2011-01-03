from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from favoritos.models import Favorito

def index(request):
    favoritos = Favorito.objects.filter(user=request.user)
    return render_to_response("profile.html", locals(), context_instance=RequestContext(request))

def salvar_favorito(request):
    if request.method == "POST":
        titulo = request.POST['titulo']
        url = request.POST['url']
        user = request.user

        favorito = Favorito.objects.create(titulo=titulo, url=url, user=user)
        favorito.save()

        return HttpResponseRedirect('/meu_delicious')
    
    