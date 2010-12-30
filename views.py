from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout, models
from django.http import HttpResponseRedirect

from favoritos.models import Favorito

def index(request):
    favoritos = Favorito.objects.all()
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

def meu_delicious_login(request):
    try:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password) 
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/meu_delicous')
    except:
        return HttpResponseRedirect('/')

def meu_delicious_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def cadastrar(request):
    username = request.POST['username']
    password = request.POST['password']

    user = models.User.objects.create(username=username)
    user.set_password(password)
    return HttpResponseRedirect('/meu_delicious')

