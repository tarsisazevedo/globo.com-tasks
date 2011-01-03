from django import forms
from django.contrib.auth.models import User

from favoritos.models import Favorito

class FavoritoForm(forms.ModelForm):
    class Meta:
        model = Favorito
        fields = ('titulo', 'url')
    
    def __init__(self, *args, **kwargs):
        super(FavoritoForm, self).__init__(*args, **kwargs)

    def clean_url(self):
        url = self.cleaned_data['url']
        return url.strip()

    def save(self, commit=True):
        favorito = super(FavoritoForm, self).save(commit=False)
        if commit:
            favorito.save()

        return favorito
