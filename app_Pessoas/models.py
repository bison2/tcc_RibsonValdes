from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE
from django.urls import reverse
# Create your models here.
#ManyToMany simples

class PessoaManager(models.Manager):

    def tudo(self):
        return self.get_queryset().order_by('nome')
    
    def prof_disc(self):
        return self.get_queryset().prefetch_related('discProf').all().order_by('nome')
    
    def aluno_disc(self):
        return self.get_queryset().prefetch_related('discAluno').all().order_by('nome')


class DisciplinaManager(models.Manager):
    
    def disciplina(self):
        return self.get_queryset().order_by('nome')

class Pessoa(models.Model):
    nome = models.CharField(max_length = 100)

    def __str__(self):
        return self.nome
    
    objects = PessoaManager()

class P_professor(Pessoa):
    cpf = models.CharField(max_length = 11)
    titulo = models.CharField(max_length =20)

class P_aluno(Pessoa):
    cpf = models.CharField(max_length = 11)
    turma = models.CharField(max_length = 20) 



class Disciplina(models.Model):
    nome = models.CharField(max_length = 30)
    professor = models.ManyToManyField("Pessoa", related_name="discProf")
    aluno = models.ManyToManyField("Pessoa", related_name="discAluno")

   
    objects = DisciplinaManager()

    def __str__(self):
        return self.nome
    
