from django.db import models
from django.contrib.auth.models import User
from django import forms

import datetime

class Favorito(models.Model):
    titulo = models.CharField(max_length=200)
    url = models.URLField(verify_exists=True)
    data = models.DateTimeField(default=datetime.datetime.now(), editable=False)
    user = models.ForeignKey(User)

    class Meta:
        ordering = ('-data',)

    def __unicode__(self):
        return self.titulo


