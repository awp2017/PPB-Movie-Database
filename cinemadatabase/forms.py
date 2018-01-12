from django import forms
from django.utils import timezone
from cinemadatabase.models import Film


class FilmForm(forms.ModelForm):

    class Meta:
        model = Film
        fields = (
            'name', 'year'
        )

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
