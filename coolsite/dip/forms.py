from django import forms
from .models import *

class PostFormAddFunctionAndSection(forms.Form):
    function = forms.CharField(max_length=255, label="Введите уравнение: ", widget=forms.TextInput(
        attrs={'class': 'custom_input',
               'placeholder': '2*x^n',
               }))

    section = forms.CharField(max_length=255, label="Введите отрезок: ", widget=forms.TextInput(
        attrs={'placeholder': '[-1.5;2]',
               'class': 'custom_input',
               }))
