from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE
from django.http import Http404

from app_questions.models import Gab, GabManager
from django.utils import timezone


# Create your models here.
#ManyToMany simples

class PessoaManager(models.Manager):

    def tudo(self):
        return self.get_queryset().order_by('nome')
    
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        instance = Pessoa.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Esse produto não existe!")
        return instance

    def prof_disc(self):
        return self.get_queryset().prefetch_related('discProf').all().order_by('nome')
    
    def aluno_disc(self):
        return self.get_queryset().prefetch_related('discAluno').all().order_by('nome')


class DisciplinaManager(models.Manager):
    
    def disciplina(self):
        return self.get_queryset().order_by('nome')
        #return Disciplina.objects.all.order_by('nome')

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None
        

class Pessoa(models.Model):
    nome = models.CharField(max_length = 100)
   

    
    objects = PessoaManager()
    
    def __str__(self):
        return self.nome
    
    def get_absolut_url(self):
        return reverse("pessoa_disc:detalhe", kwargs={"id": self.id})
       
 

class P_professor(Pessoa):
    cpf = models.CharField(max_length = 11)
    titulo = models.CharField(max_length =20)

class P_aluno(Pessoa):
    cpf = models.CharField(max_length = 11)
    turma = models.CharField(max_length = 20) 



class Disciplina(models.Model):
    nome = models.CharField(max_length = 30)
    data_inicio = models.DateTimeField( null=True, blank=True)
    data_fim = models.DateTimeField( null=True, blank=True)
    info=models.TextField(null=True, blank=True)   
   # description = models.TextField()
    #inicio =  models.DateTimeField(auto_now=True, null = True, blank = True)
    #final =  models.DateTimeField(auto_now_add=True, null = True, blank = True)

    professor = models.ManyToManyField("Pessoa", related_name="discProf")
    aluno = models.ManyToManyField("Pessoa", related_name="discAluno")
    #questao = models.ForeignKey("Gab", on_delete=CASCADE, related_name="discq")
   
    objects = DisciplinaManager()

    def __str__(self):
        return self.nome
    
