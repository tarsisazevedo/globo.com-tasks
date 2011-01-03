from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from forms import CadastroForm

def cadastrar(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            novo_usuario = form.save()        
            return HttpResponseRedirect('/meu_delicious')
    else:
        form = CadastroForm()
    return render_to_response('cadastro.html', {'form': form}, context_instance=RequestContext(request))

