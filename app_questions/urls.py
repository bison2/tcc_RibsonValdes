from django.urls import path, include 
from .views import question, gabarito, confere
#from app_Pessoas.views import Disciplina, Pessoa, P_professor, P_aluno


app_name= 'questions'
urlpatterns =[
   
    path('', question, name='question'),
    path('resposta/', gabarito, name='resposta'),
    path('confere/', confere, name='confere'),
]