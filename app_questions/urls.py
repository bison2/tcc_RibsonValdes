from django.urls import path, include 
from . import views
from django.conf.urls import url

#from app_questions import views
#from app_Pessoas.views import Disciplina, Pessoa, P_professor, P_aluno


app_name="questions"
urlpatterns =[
   
    path('', views.question, name='question'),
    path('resposta/', views.gabarito, name='resposta'),
    path('confere/', views.confere, name='confere'),
    #url(r'^confere$', views.confere, name='confere'),
]