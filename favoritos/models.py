from django.db import models
from django.contrib.auth.models import User, UserManager
from django.db.models import signals

class Favorito(models.Model):
    titulo = models.CharField(max_length=200)
    url = models.URLField()

    def __unicode__(self):
        return self.titulo

class Usuario(models.Model):
    favoritos = models.ForeignKey(Favorito, blank=True, null=True)
    user = models.OneToOneField('auth.User', related_name='profile')

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(user=instance)
signals.post_save.connect(create_user_profile, sender=Usuario)
