from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse 
from django.contrib.auth.decorators import login_required

from favoritos.models import Favorito
from favoritos.forms import FavoritoForm

@login_required
def index(request):
    favoritos = Favorito.objects.filter(user=request.user)
    return render_to_response("profile.html", locals(), context_instance=RequestContext(request))

def novo_favorito(request):
    if request.method == "POST":
        form =  FavoritoForm(request.POST) 
        if form.is_valid():
            form.set_user(request.user)
            favorito = form.save()
            return HttpResponseRedirect('/meu_delicious')
    else:
        form = FavoritoForm()
    return render_to_response("favoritos/favorito_form.html", locals(), context_instance=RequestContext(request))
            
    
