#encoding: utf-8
from django import forms
from django.contrib.auth.models import User

class CadastroForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password')

    confirme_a_senha = forms.CharField(max_length=30, widget=forms.PasswordInput) 

    def __init__(self, *args, **kwargs):
        self.base_fields['password'].help_text = 'Informe uma senha segura'
        self.base_fields['password'].widget = forms.PasswordInput()
        super(CadastroForm, self).__init__(*args, **kwargs)

    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data['username'],).count():
            raise forms.ValidationError('Ja existe um usuario com este username')
                 
        return self.cleaned_data['username']
                        
    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email'],).count():
            raise forms.ValidationError('Ja existe um usuario com este e-mail')
                                                
        return self.cleaned_data['email']
                                                    
    def clean_confirme_a_senha(self):
        if self.cleaned_data['confirme_a_senha'] != self.data['password']:
            raise forms.ValidationError('Confirmacao da senha nao confere!')
                                                                    
        return self.cleaned_data['confirme_a_senha']
                                                                        
    def save(self, commit=True):
        usuario = super(CadastroForm, self).save(commit=False)                                 
        usuario.set_password(self.cleaned_data['password'])
                                                                                            
        if commit:
            usuario.save()
                                                                                                                    
        return usuario
