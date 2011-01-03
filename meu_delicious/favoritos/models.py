from django.db import models
from django.contrib.auth.models import User

import datetime

class Favorito(models.Model):
    titulo = models.CharField(max_length=200)
    url = models.URLField()
    data = models.DateField(default=datetime.datetime.now())
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.titulo