from django.shortcuts import render
from .models import Pessoa, Disciplina , P_professor, P_aluno

# Create your views here.

def home(request):
    pessoa_data = Pessoa.objects.tudo()
    prof_data = P_professor.objects.prof_disc()
    aluno_data = P_aluno.objects.tudo()
    disciplina_data = Disciplina.objects.disciplina()
    
    disc_prof_data = P_professor.objects.prof_disc()
    disc_aluno_data = P_aluno.objects.aluno_disc()
    

    return render(request, 'app_Pessoas/pessoas.html', {
                    'pessoas':pessoa_data,
                    'professores': prof_data,
                    'alunos': aluno_data,

                    'disciplinas': disciplina_data,
                    
                    'disc_prof': disc_prof_data,
                    'disc_aluno': disc_aluno_data,
                    }
            )

