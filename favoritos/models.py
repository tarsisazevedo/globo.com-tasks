from django.db import models

class Favorito(models.Model):
    titulo = models.CharField(max_length=200)
    url = models.URLField()

    def __unicode__(self):
        return self.titulo
