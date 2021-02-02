from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.views.generic import ListView, DetailView
from .models import Pessoa, Disciplina , P_professor, P_aluno
from django.contrib.auth.models import User
# Create your views here.

def home_pessoa(request):
    pessoa_data = Pessoa.objects.tudo()
    prof_data = P_professor.objects.prof_disc()
    aluno_data = P_aluno.objects.tudo()
    disciplina_data = Disciplina.objects.disciplina()
    
    disc_prof_data = P_professor.objects.prof_disc()
    disc_aluno_data = P_aluno.objects.aluno_disc()
    

    return render(request, 'app_Pessoas/lista.html', {
                    'pessoas':pessoa_data,
                    'professores': prof_data,
                    'alunos': aluno_data,

                    'disciplinas': disciplina_data,
                    
                    'disc_prof': disc_prof_data,
                    'disc_aluno': disc_aluno_data,
                    }
            )


def pessoa_id(request, id):
    obj = Pessoa.objects.get(id=id)
    
    context = {
               
               'pessoa':obj,
               
               }
    return render(request, 'app_Pessoas/detalhe.html', context)


