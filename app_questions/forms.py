from django import forms
from django.contrib.auth import get_user_model




escolha_anos = ['2019', '2020', '2021', '1972']
escolha_cores = [('azul', 'Azul'),
                  ('red', 'Red'),
                  ('verde', 'Verde'),
                ]
escolha_respostas = [('verdadeiro','Verdadeiro'),
                     ('falso', 'Falso'),
                    ]
class QuestionForm(forms.Form):
    question = forms.CharField(
        widget=forms.TextInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "digite sua pergunta"
                }
            )
        )
    data = forms.DateField(
        widget=forms.SelectDateWidget( years=escolha_anos)
        )
    cores = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
            choices=escolha_cores)

    resposta = forms.MultipleChoiceField(
        widget=forms.SelectMultiple,
            choices=escolha_respostas)

class GabaritoForm(forms.Form):
    gabarito = forms.CharField(
        widget=forms.TextInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "digite o gabarito"
                }
            )
        )
             
    
    
    