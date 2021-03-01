from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.views.generic import ListView, DetailView
from .models import Pessoa, Disciplina , P_professor, P_aluno
from django.contrib.auth.models import User

# Create your views here.

def home_disciplina(request):
    #pessoa_data = Pessoa.objects.tudo()
    #prof_data = P_professor.objects.prof_disc()
    #aluno_data = P_aluno.objects.tudo()
    disciplina_data = Disciplina.objects.disciplina()
    
    #disc_prof_data = P_professor.objects.prof_disc()
    #disc_aluno_data = P_aluno.objects.aluno_disc()
    
    return render(request, 'app_Pessoas/lista_disciplina.html', {
                    #'pessoas':pessoa_data,
                    #'professores': prof_data,
                    #'alunos': aluno_data,

                    'disciplinas': disciplina_data,
                    
                    #'disc_prof': disc_prof_data,
                    #'disc_aluno': disc_aluno_data,
                    }
            )

def home_professor(request):
   # pessoa_data = Pessoa.objects.tudo()
    prof_data = P_professor.objects.prof_disc()
    #aluno_data = P_aluno.objects.tudo()
    #disciplina_data = Disciplina.objects.disciplina()
    
    disc_prof_data = P_professor.objects.prof_disc()
    #disc_aluno_data = P_aluno.objects.aluno_disc()
    
    return render(request, 'app_Pessoas/lista_professor.html', {
                    #'pessoas':pessoa_data,
                    'professores': prof_data,
                    #'alunos': aluno_data,

                    #'disciplinas': disciplina_data,
                    
                    'disc_prof': disc_prof_data,
                    #'disc_aluno': disc_aluno_data,
                    }
            )

def home_aluno(request):
   # pessoa_data = Pessoa.objects.tudo()
    #prof_data = P_professor.objects.prof_disc()
    aluno_data = P_aluno.objects.tudo()
    #disciplina_data = Disciplina.objects.disciplina()
    
    #disc_prof_data = P_professor.objects.prof_disc()
    disc_aluno_data = P_aluno.objects.aluno_disc()
    
    return render(request, 'app_Pessoas/lista_aluno.html', {
                    #'pessoas':pessoa_data,
                    #'professores': prof_data,
                    'alunos': aluno_data,

                    #'disciplinas': disciplina_data,
                    
                    #'disc_prof': disc_prof_data,
                    'disc_aluno': disc_aluno_data,
                    }
            )

def pessoa_id(request, id):
    obj = Pessoa.objects.get(id=id)
    
    context = {
               
               'pessoa':obj,
               
               }
    return render(request, 'app_Pessoas/detalhe.html', context)

def disciplina_id(request, id):
    obj = Disciplina.objects.get(id=id)
    
    context = {
               
               'disciplina':obj,
               
               }
    return render(request, 'app_Pessoas/detalhe_disciplina.html', context)

def professor_id(request, id):
    obj = P_professor.objects.get(id=id)
    disc_prof_data = P_professor.objects.get(id=id)
    #disc_prof_data = P_professor.objects.prof_disc()
    context = {
               'disc_prof':disc_prof_data,
               'pessoa':obj,
               
               }
    return render(request, 'app_Pessoas/detalhe_professor.html', context)

def aluno_id(request, id):
    obj = P_aluno.objects.get(id=id)
    disc_aluno_data = P_aluno.objects.get(id=id)
    #disc_prof_data = P_professor.objects.prof_disc()
    context = {
               'disc_aluno':disc_aluno_data,
               'pessoa':obj,
               
               }
    return render(request, 'app_Pessoas/detalhe_aluno.html', context)