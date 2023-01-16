from django import forms
from .models import *

class PostFormAddFunctionAndSection(forms.Form):

    # Функция
    function = forms.CharField(max_length=255, label="Введите уравнение: ", widget=forms.TextInput(
        attrs={'class': 'custom_input',
               'placeholder': '2*x^n',
               }))


    # Отрезок
    section = forms.CharField(max_length=255, label="Введите отрезок: ", widget=forms.TextInput(
        attrs={'placeholder': '[-1.5;2]',
               'class': 'custom_input',
               }))


    # Параметры метода
    par_small = forms.CharField(max_length=255, label=u"\u03bc: ", widget=forms.TextInput(
        attrs={'class': 'custom_input',
               'placeholder': '0.01',
               }))

    par_step = forms.CharField(max_length=255, label="h: ", widget=forms.TextInput(
        attrs={'placeholder': '0.0001',
               'class': 'custom_input',
               }))


    # Погрешности метода
    pogr_eps = forms.CharField(max_length=255, label=u"\u03b5: ", widget=forms.TextInput(
        attrs={'class': 'custom_input',
               'placeholder': '0.0001',
               }))

    pogr_delta = forms.CharField(max_length=255, label=u"\u03b4: ", widget=forms.TextInput(
        attrs={'placeholder': '0.0001',
               'class': 'custom_input',
               }))


# class FormParametersAndInaccuracy(forms.Form):
#
#     # Параметры метода
#     par_small = forms.CharField(max_length=255, label=u"\u03bc: ", widget=forms.TextInput(
#         attrs={'class': 'custom_input',
#                'placeholder': '2*x^n',
#                }))
#
#     par_step = forms.CharField(max_length=255, label="h: ", widget=forms.TextInput(
#         attrs={'placeholder': '[-1.5;2]',
#                'class': 'custom_input',
#                }))
#
#
#     # Погрешности метода
#     pogr_eps = forms.CharField(max_length=255, label=u"\u03b5: ", widget=forms.TextInput(
#         attrs={'class': 'custom_input',
#                'placeholder': '2*x^n',
#                }))
#
#     pogr_delta = forms.CharField(max_length=255, label=u"\u03b4: ", widget=forms.TextInput(
#         attrs={'placeholder': '[-1.5;2]',
#                'class': 'custom_input',
#                }))