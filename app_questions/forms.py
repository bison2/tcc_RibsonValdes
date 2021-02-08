from django import forms
from django.contrib.auth import get_user_model
from .models import Gab
from django.forms.widgets import RadioSelect

class GabForm(forms.ModelForm):

    class Meta:
        model = Gab 
        fields =[
                'alternativa',
                'resposta',
                'alternativa2',
        ]
        widgets = { 
           'alternativa2':RadioSelect
        }       
       # gabarito = forms.CharField(
        #3widget=forms.TextInput(
         #  attrs={
          #          "class": "form-control", 
           #         "placeholder": "digite o gabarito"
            #    }
            #)
        #)



escolha_anos = ['2019', '2020', '2021', '1972']
escolha_cores = [('azul', 'Azul'),
                  ('red', 'Red'),
                  ('verde', 'Verde'),
                ]
escolha_respostas = [('verdadeiro','Verdadeiro'),
                     ('falso', 'Falso'),
                     ('25', '25'),
                     ('30%', '30%'),
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
        widget=forms.RadioSelect,
        choices=escolha_respostas)
    
    
    
    
    gabarito = forms.CharField(
        widget=forms.TextInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "digite o gabarito"
                }
            )
        )
        

             
    
    
    