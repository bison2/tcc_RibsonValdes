from django.urls import path, include 
from django.conf.urls import url
from .views import home_disciplina, disciplina_id, home_professor, professor_id, home_aluno, aluno_id, pessoa_id

app_name= 'pessoa_disc'
urlpatterns =[
    #url(r'^homepessoa$', home_pessoa, name='homepessoa'),
    path('', home_disciplina, name='homedisciplina'),
    path('<int:id>/', pessoa_id , name='detalhe'),
    path('disc/<int:id>/', disciplina_id , name='detalhedisciplina'),
    path('prof/', home_professor, name='homeprofessor'),
    path('prof/<int:id>/', professor_id , name='detalheprofessor'),
    path('aluno/', home_aluno, name='homealuno'),
    path('aluno/<int:id>/', aluno_id , name='detalhealuno'),
    
    #url(r'^(?P<id>\d+)$', pessoa_id, name='detalhe')
   #erro ao passar o id-url-> [\w]
]