from django import forms
from django.contrib.auth import get_user_model
from .models import Gab
from django.forms.widgets import RadioSelect

class GabForm(forms.ModelForm):

    class Meta:
        model = Gab 
        fields =[
            #    'alternativa',
                'resposta',
            #    'alternativa2',
                
        ]
        widgets = { 
        #   'alternativa2':RadioSelect,
           'resposta':RadioSelect
         
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
    
    resposta22 = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=escolha_respostas)

    cores = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
            choices=escolha_cores)

    gabarito = forms.CharField(
        widget=forms.TextInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "digite o gabarito"
                }
            )
        )
        

             
    
    
    