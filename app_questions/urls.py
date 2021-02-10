from django.urls import path, include 
from . import views
from django.conf.urls import url

#from app_questions import views
#from app_Pessoas.views import Disciplina, Pessoa, P_professor, P_aluno


app_name="questions"
urlpatterns =[
   
    path('', views.question, name='question'),
    path('q22/', views.radio, name='question22'),
    path('resposta/<int:id>/', views.gabarito, name='resposta'),
    path('confere/<gabarito>/<resposta>/<msg>/', views.confere, name='confere'),
    #url(r'^confere$', views.confere, name='confere'),
]