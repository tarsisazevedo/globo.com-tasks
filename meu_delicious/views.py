from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout, models
from django.http import HttpResponseRedirect
from django.db import IntegrityError

from favoritos.models import Favorito
from forms import LoginForm, CadastroForm

def index(request):
    favoritos = Favorito.objects.all()
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))
            
def meu_delicious_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password) 
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/meu_delicious')
    else:
        form = LoginForm()
        return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))

def meu_delicious_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def cadastrar(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            first_name= form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            try:
                user = models.User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name)
                user.set_password(password)
                user.save()
            except IntegrityError:
                mensagem_erro = "Usuario ja existe."
                return render_to_response('cadastro.html', {'mensagem_erro': mensagem_erro}, context_instance=RequestContext(request))
            
            return HttpResponseRedirect('/meu_delicious')
    else:
        form = CadastroForm()
        return render_to_response('cadastro.html', {'form': form}, context_instance=RequestContext(request))

