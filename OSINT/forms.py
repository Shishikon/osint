
from django import forms
from .models import TelegramSearch, GitHubSearch


class WebSurferForm(forms.Form):
    link = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter a link'
        }
    ))



class TelegramForm(forms.ModelForm):

    class Meta:
        model = TelegramSearch

        fields = ['searched_username']

        widgets = {
            'searched_username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter username'
                }
            )
        }




class GitHubForm(forms.ModelForm):

    class Meta:
        model = GitHubSearch

        fields = ['searched_username']

        widgets = {
            'searched_username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter username'
                }
            )
        }