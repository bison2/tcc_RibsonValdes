from django.urls import path, include 
from django.conf.urls import url
from .views import home_pessoa, pessoa_detail, pessoa_id, PessoaDetailView

app_name= 'pessoa_disc'
urlpatterns =[
    #url(r'^homepessoa$', home_pessoa, name='homepessoa'),
    path('', home_pessoa, name='homepessoa'),
    path('<int:id>/', pessoa_id , name='detalhe'),
    #url(r'^(?P<id>\d+)$', pessoa_id, name='detalhe')
   #erro ao passar o id-url-> [\w]
]