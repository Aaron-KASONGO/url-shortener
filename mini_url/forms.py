from django.forms import ModelForm
from django import forms
from .models import MiniUrl
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User


class MiniUrlForm(ModelForm):
    class Meta:
        model = MiniUrl
        fields = ('url', 'pseudo')


class UserForm(ModelForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(widget=forms.EmailInput())
    password = forms.CharField(label='Mot de passe', max_length=100, widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirmer le Mot de passe', max_length=100, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def clean_password2(self):
        pwd1 = self.cleaned_data.get('password')
        pwd2 = self.cleaned_data.get('password2')
        if pwd1 != pwd2:
            raise forms.ValidationError("Mots de passe incompatibles")
        else:
            return pwd1

    def save(self, commit=True, *args, **kwargs):
        m = super(UserForm, self).save(commit=False)
        m.password = make_password(self.cleaned_data.get("password"))
        m.username = self.cleaned_data.get("username")
        if commit:
            m.save()
        return m


class SigninForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('Nom d\'utilisateur ou Mot de passe incorrect')
        else:
            user = User.objects.get(username=username)
            if not check_password(password, user.password):
                raise forms.ValidationError('Nom d\'utilisateur ou Mot de passe incorrect')
"""
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', '')"""
