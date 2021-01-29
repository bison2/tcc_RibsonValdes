from django.urls import path, include 
from django.conf.urls import url 
from .views import home_pessoa, pessoa_detail, pessoa_id

app_name= 'pessoa_disc'
urlpatterns =[
    #url(r'^homepessoa$', views.home_pessoa, name='homepessoa'),
    path('', home_pessoa, name='homepessoa'),
    path('<int:id>', pessoa_detail, name='detalhe'),
    #url(r'^detalhe/(?P<id>\d+)$', views.pessoa_id, name='detalhe')
]